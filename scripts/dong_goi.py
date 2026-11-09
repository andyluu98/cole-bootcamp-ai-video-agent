# -*- coding: utf-8 -*-
"""Đóng gói file tải về cho web: tai-ve/du-an-mau.zip (thư mục dự án kèm bộ buổi 1)
và tai-ve/buoi-0N.zip (bộ cài từng buổi). Chạy: python scripts/dong_goi.py"""
import pathlib
import zipfile

GOC = pathlib.Path(__file__).resolve().parent.parent
DU_AN = GOC / "du-an-mau"
RA = GOC / "tai-ve"
RA.mkdir(exist_ok=True)

# du-an-mau.zip: mọi file trong du-an-mau, bỏ bộ cài buổi 2 trở đi; giải nén ra thư mục du-an-video
file_zip = RA / "du-an-mau.zip"
with zipfile.ZipFile(file_zip, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(DU_AN.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(DU_AN)
        if rel.parts[:1] == ("bo-cai",) and len(rel.parts) > 1 and rel.parts[1] != "buoi-01":
            continue
        z.write(f, pathlib.Path("du-an-video") / rel)
print("OK", file_zip)

# buoi-0N.zip: nội dung bo-cai/buoi-0N, giải nén ra thư mục buoi-0N
for thu_muc in sorted((DU_AN / "bo-cai").glob("buoi-*")):
    if thu_muc.name == "buoi-01":
        continue
    file_zip = RA / f"{thu_muc.name}.zip"
    with zipfile.ZipFile(file_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(thu_muc.rglob("*")):
            if f.is_file():
                z.write(f, pathlib.Path(thu_muc.name) / f.relative_to(thu_muc))
    print("OK", file_zip)
