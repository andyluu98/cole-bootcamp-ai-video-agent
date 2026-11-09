// Nút "Chép" cho mọi khối prompt; đánh dấu mục menu đang mở.
document.querySelectorAll('.prompt').forEach(function (box) {
  var btn = box.querySelector('button');
  var text = box.querySelector('p');
  if (!btn || !text) return;
  btn.addEventListener('click', function () {
    navigator.clipboard.writeText(text.innerText).then(function () {
      btn.textContent = 'Đã chép';
      btn.classList.add('ok');
      setTimeout(function () { btn.textContent = 'Chép'; btn.classList.remove('ok'); }, 1800);
    });
  });
});
var here = location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('nav.top a').forEach(function (a) {
  if (a.getAttribute('href') === here) a.classList.add('on');
});
