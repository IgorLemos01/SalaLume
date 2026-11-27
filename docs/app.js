(function(){
  // cabeçalho
  var top=document.getElementById('top');
  var onScroll=function(){top.classList.toggle('scrolled',window.scrollY>8)};
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  var mb=document.getElementById('menu-btn'),nav=document.getElementById('nav');
  mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o);mb.setAttribute('aria-label',o?'Fechar menu':'Abrir menu')});

  // abas
  var tabs=[].slice.call(document.querySelectorAll('[role=tab]'));
  function select(t,focus){tabs.forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;document.getElementById(x.getAttribute('aria-controls')).hidden=!on});if(focus)t.focus()}
  tabs.forEach(function(t,i){
    t.addEventListener('click',function(){select(t)});
    t.addEventListener('keydown',function(e){var k=e.key,n=null;if(k==='ArrowRight')n=tabs[(i+1)%tabs.length];if(k==='ArrowLeft')n=tabs[(i-1+tabs.length)%tabs.length];if(k==='Home')n=tabs[0];if(k==='End')n=tabs[tabs.length-1];if(n){e.preventDefault();select(n,true)}});
  });
  document.querySelectorAll('[data-decide]').forEach(function(b){b.addEventListener('click',function(){b.closest('.mock').querySelector('.decide-msg').textContent=b.getAttribute('data-decide')})});

  // formulário
  var form=document.getElementById('form');
  if(!form)return;
  var rules={nome:function(v){return v.trim()?'':'Informe seu nome.'},cargo:function(v){return v?'':'Selecione seu cargo.'},escola:function(v){return v.trim()?'':'Informe a escola ou rede.'},email:function(v){return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim())?'':'Informe um e-mail válido, como nome@escola.com.br.'}};
  function check(name){var el=form.elements[name],msg=rules[name](el.value),f=el.closest('.field');f.classList.toggle('invalid',!!msg);el.setAttribute('aria-invalid',!!msg);document.getElementById('e-'+name).textContent=msg;if(msg)el.setAttribute('aria-describedby','e-'+name);return !msg}
  Object.keys(rules).forEach(function(n){form.elements[n].addEventListener('blur',function(){if(form.elements[n].value)check(n)})});
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var bad=Object.keys(rules).filter(function(n){return !check(n)});
    if(bad.length){form.elements[bad[0]].focus();return}
    document.getElementById('done-msg').textContent='Obrigado, '+form.elements.nome.value.trim().split(' ')[0]+'. Seus dados estão prontos para a equipe da Sala Lume combinar a apresentação pelo e-mail '+form.elements.email.value.trim()+'.';
    document.getElementById('form-body').hidden=true;
    document.getElementById('form-done').hidden=false;
  });
})();
