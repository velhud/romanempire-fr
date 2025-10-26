(function(){
  "use strict";

  const translationsEl = document.getElementById('translations');

  function loadTranslations(){
    if(!translationsEl) return {};
    try{
      const raw = translationsEl.textContent || translationsEl.innerText || '';
      return raw ? JSON.parse(raw) : {};
    }catch(err){
      console.error('Failed to parse translations JSON', err);
      return {};
    }
  }

  const translations = loadTranslations();
  const defaultLang = translations.en ? 'en' : Object.keys(translations)[0] || 'en';
  const storageKey = 'romanempire-lang';
  const langBtns = document.querySelectorAll('.lang-btn');
  const captionKeyMap = {
    'iz-drysha-v-atlety': 'drysh',
    'franco-columbu': 'franco',
    'everbet': 'everbet',
    'i-pressa': 'ipressa',
    'copycat': 'copycat',
    'airrods': 'airrods',
    'rgau-mskha': 'rgau',
    'studgorodok-rgau': 'studgorodok',
    'diplosha': 'diplosha',
    'universite-catholique-de-lille': 'ucl',
    'euratechnologies': 'euratechnologies'
  };

  function safeGet(key){
    try{
      return window.localStorage.getItem(key);
    }catch(err){
      return null;
    }
  }

  function safeSet(key, value){
    try{
      window.localStorage.setItem(key, value);
    }catch(err){
      /* no-op */
    }
  }

  function detectLanguage(){
    const stored = safeGet(storageKey);
    if(stored && translations[stored]) return stored;
    const browser = navigator.language ? navigator.language.split('-')[0] : '';
    if(browser && translations[browser]) return browser;
    return defaultLang;
  }

  let currentLang = detectLanguage();

  function formatValue(value){
    if(typeof value === 'string' && value.indexOf('{brand}') !== -1){
      return value.replace('{brand}', '<span class="brand">in<span class="A">A</span>i.fr</span>');
    }
    return value == null ? '' : value;
  }

  function setHTML(el, value){
    if(!el || value == null) return;
    el.innerHTML = formatValue(value);
  }

  function setText(el, value){
    if(!el || value == null) return;
    el.textContent = formatValue(value);
  }

  function setAttr(el, attr, value){
    if(!el || value == null) return;
    el.setAttribute(attr, value);
  }

  function updateMeta(meta){
    if(!meta) return;
    const title = meta.title || '';
    const description = meta.description || '';
    if(title) document.title = title;
    function writeMeta(selector, attr, value){
      if(value == null) return;
      const tag = document.querySelector(selector);
      if(tag) tag.setAttribute(attr, value);
    }
    writeMeta("meta[name='description']", 'content', description);
    writeMeta("meta[property='og:title']", 'content', title);
    writeMeta("meta[property='og:description']", 'content', description);
    writeMeta("meta[name='twitter:title']", 'content', title);
    writeMeta("meta[name='twitter:description']", 'content', description);
  }

  function updateHero(hero){
    if(!hero) hero = {};
    setText(document.querySelector('.hero h1'), hero.greeting);
    setHTML(document.querySelector('.lead'), hero.lead);

    const blocks = document.querySelectorAll('.hero .block');
    const blockKeys = ['block1', 'block2', 'block3', 'block4', 'block5'];
    blockKeys.forEach(function(key, idx){
      const block = blocks[idx];
      if(!block) return;
      if(idx < 3){
        setHTML(block, hero[key]);
      }else{
        setText(block, hero[key]);
      }
    });

    const primaryBtn = document.querySelector('.btn:not(.btn-ghost)');
    if(primaryBtn){
      const btnText = hero.btn_try || '';
      const brandSpan = primaryBtn.querySelector('.btn-brand');
      if(brandSpan){
        let textNode = Array.from(primaryBtn.childNodes).find(function(node){
          return node.nodeType === Node.TEXT_NODE;
        });
        if(!textNode){
          textNode = document.createTextNode('');
          primaryBtn.insertBefore(textNode, brandSpan);
        }
        textNode.textContent = btnText ? btnText + ' ' : '';
      }else{
        setText(primaryBtn, btnText);
      }
      if(btnText){
        primaryBtn.setAttribute('aria-label', btnText);
      }
    }

    const ghostBtns = document.querySelectorAll('.btn-ghost');
    const ghostKeys = ['btn_skills', 'btn_cv', 'btn_education'];
    ghostBtns.forEach(function(btn, idx){
      const key = ghostKeys[idx];
      const value = hero[key];
      if(value != null){
        btn.textContent = formatValue(value);
        btn.setAttribute('aria-label', formatValue(value));
      }
    });

    setText(document.querySelector('.contact-label'), hero.contact_label);
  }

  function updatePillars(pillars){
    if(!pillars) pillars = {};
    setText(document.querySelector('.pillars .section-title'), pillars.title);
    setAttr(document.querySelector('.pillars'), 'aria-label', pillars.title);
    const pillarButtons = document.querySelectorAll('.pillars .pillar');
    pillarButtons.forEach(function(btn){
      const slug = btn.getAttribute('data-pillar');
      let nameKey = '';
      let noteKey = '';
      switch(slug){
        case 'franco-columbu':
          nameKey = 'franco_name';
          noteKey = 'franco_note';
          break;
        case 'inai':
          nameKey = 'inai_name';
          noteKey = 'inai_note';
          break;
        case 'i-pressa':
          nameKey = 'ipressa_name';
          noteKey = 'ipressa_note';
          break;
        case 'universite-catholique-de-lille':
          nameKey = 'ucl_name';
          noteKey = 'ucl_note';
          break;
        default:
          break;
      }
      if(!nameKey) return;
      const name = pillars[nameKey];
      const note = pillars[noteKey];
      setText(btn.querySelector('.pillar-name'), name);
      setText(btn.querySelector('.pillar-note'), note);
      if(note) btn.setAttribute('aria-label', note);
    });
  }

  function updateShowcase(showcase){
    if(!showcase) showcase = {};
    setText(document.querySelector('.showcase .section-title'), showcase.title);
    const slider = document.querySelector('.slider');
    if(slider && showcase.title){
      slider.setAttribute('aria-label', showcase.title);
    }
    setAttr(document.querySelector('.arrow.left'), 'aria-label', showcase.prev);
    setAttr(document.querySelector('.arrow.right'), 'aria-label', showcase.next);
  }

  function updateBadgesAndCaptions(data){
    const captions = (data && data.captions) || {};
    const badges = (data && data.badges) || {};
    document.querySelectorAll('.logo-card[data-slug]').forEach(function(card){
      const slug = card.dataset.slug;
      const key = captionKeyMap[slug] || slug;
      const caption = captions[key];
      if(caption){
        card.dataset.caption = caption;
        card.setAttribute('aria-label', caption);
      }
      setText(card.querySelector('.badge-archived'), badges.archived);
      setText(card.querySelector('.badge-active'), badges.active);
    });

    const inaiBadge = document.querySelector('.inai .badge-outcome');
    setText(inaiBadge, badges.outcome);
  }

  function resetTooltip(){
    const tooltip = document.querySelector('.tooltip');
    if(tooltip){
      tooltip.classList.remove('show', 'above', 'below');
      tooltip.textContent = '';
      tooltip.style.transform = 'translate(-9999px,-9999px)';
    }
  }

  function updateLangButtons(){
    langBtns.forEach(function(btn){
      const isActive = btn.dataset.lang === currentLang;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });
  }

  function applyTranslations(options){
    const data = translations[currentLang] || translations[defaultLang] || {};
    const emitEvent = !options || options.emitEvent !== false;
    updateMeta(data.meta);
    updateHero(data.hero);
    updatePillars(data.pillars);
    updateShowcase(data.showcase);
    updateBadgesAndCaptions(data);
    updateLangButtons();
    document.documentElement.lang = currentLang;
    safeSet(storageKey, currentLang);
    resetTooltip();
    if(emitEvent){
      window.dispatchEvent(new CustomEvent('romanempire:langchange'));
    }
  }

  function switchLanguage(lang){
    if(!lang || !translations[lang] || lang === currentLang) return;
    currentLang = lang;
    applyTranslations({emitEvent:false});
    window.dispatchEvent(new CustomEvent('romanempire:langchange'));
  }

  langBtns.forEach(function(btn){
    btn.addEventListener('click', function(){
      switchLanguage(btn.dataset.lang);
    });
  });

  applyTranslations();

  window.RomanEmpireI18n = {
    get current(){ return currentLang; },
    data: translations,
    switch: switchLanguage,
    apply: applyTranslations
  };
})();
