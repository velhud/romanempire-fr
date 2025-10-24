import json
from pathlib import Path

translations = {
  "en": {
    "meta": {
      "title": "Roman Empire",
      "description": "Welcome to Roman and his Empire. A minimal, ironic one-page empire."
    },
    "hero": {
      "greeting": "Hi.",
      "lead": "You’ve probably been thinking about the Roman Empire.<br>Congratulations. You found one.",
      "block1": "This Roman is building an empire across the world and across disciplines.<br>It is wide and multidimensional. He can build one for you too.",
      "block2": "But let’s not dwell on the past. Empires rise and fall.<br><strong>Better to try {brand}. They are building the future.</strong>",
      "block3": "Yet, if you still wish to find what Roman offers, here is what you get:",
      "block4": "I turn scattered fronts into a single campaign that ships.",
      "block5": "Built a multi-site business · University lecturer · Personal agent and representation",
      "btn_try": "Try",
      "btn_skills": "Artes",
      "btn_cv": "Cursus Honorum",
      "btn_education": "Studia",
      "btn_aria": {
        "try": "Try inAi",
        "skills": "Open Skills",
        "cv": "Open CV",
        "education": "Open Education"
      },
      "contact_label": "⟨ Proposals and introductions ⟩"
    },
    "pillars": {
      "title": "Four Pillars of Empire",
      "items": [
        {"name": "Franco Columbu", "note": "Verified presence, translations, and press operations."},
        {"name": "inAi", "note": "Independent build from concept to product."},
        {"name": "iPressa", "note": "Zero-to-one to three sites; continuity under stress."},
        {"name": "Université Catholique de Lille", "note": "Taught and ran a program at a French university."}
      ]
    },
    "showcase": {
      "title": "History of Empire",
      "prev": "Previous",
      "next": "Next",
      "region": "Project logos"
    },
    "badges": {
      "archived": "Archived",
      "active": "Active",
      "outcome": "Built + incubated"
    },
    "captions": {
      "iz-drysha-v-atlety": "Early media experiment on disciplined transformation; ended after initial sprint.",
      "franco-columbu": "Agent in Russia/E. Europe; verified VK, translations, fan community, press.",
      "everbet": "Short-run math-driven predictions prototype; closed after trials.",
      "i-pressa": "Print/copy business from zero to three offices; COVID continuity; social-commerce ops.",
      "copycat": "Brand split to widen choice with a single back office; physical site in Khimki.",
      "airrods": "Instagram-based AirPods store; media-led acquisition and local delivery.",
      "rgau-mskha": "Coach → gym operations manager; eight sites; renovation and reopen plan.",
      "studgorodok-rgau": "Unofficial residences hub adopted by management; ~4.5k members.",
      "diplosha": "Thesis-support spin-out; 3–4 deliveries; paused on relocation.",
      "universite-catholique-de-lille": "Genetics lecturer; course delivered; international student support.",
      "euratechnologies": "Incubation accelerating inAi; Retail & E-commerce track."
    },
    "inaiSpotlight": {
      "aria": "Open the inAi case"
    },
    "aria": {
      "lang_switcher": "Language selector",
      "portrait_alt": "Portrait of Roman Chuikov",
      "portrait_caption": "Portrait of Roman Chuikov",
      "modal_close": "Close"
    },
    "modals": {
      "cv": {
        "title": "Cursus Honorum",
        "summary": "Builder‑operator across disciplines.<br>Based in France. Focus: inAi.<br>When to hire: audit, launch, rescue.",
        "campaignsTitle": "Campaigns",
        "campaigns": [
          {
            "role": "Founder",
            "company": "inAi",
            "meta": "Jun 2025–present · Lille, France · Venture · Primary",
            "body": "General-purpose AI agent. Team of 3. Reliability, cost control, and handover discipline."
          },
          {
            "role": "Participant",
            "company": "EuraTechnologies (incubation)",
            "meta": "Sep 2025–present · Lille, France · Retail & E-commerce track",
            "body": "Incubation supporting inAi milestones, discovery, and partner lanes. Proof available by email."
          },
          {
            "role": "Lecturer",
            "company": "Université Catholique de Lille",
            "meta": "Aug 2022–Sep 2023 · Lille, France · Employment",
            "body": "Delivered genetics course and supported international programs. Materials on request."
          },
          {
            "role": "Co-creator",
            "company": "AirRods (AirPods store)",
            "meta": "Nov 2019–Mar 2021 · Moscow, Russia · Venture · Side",
            "body": "Instagram-based storefront. Roman ran media, content, and fulfillment ops."
          },
          {
            "role": "Initiator",
            "company": "Диплошa (Diplosha)",
            "meta": "May 2020–Jul 2021 · Moscow, Russia · Venture · Side",
            "body": "Thesis support spin-out from existing student clients; paused on relocation."
          },
          {
            "role": "Founder",
            "company": "Студгородок (Student Residences)",
            "meta": "Nov 2019–Apr 2020 (handover) · Moscow, Russia · Venture · Side",
            "body": "Unofficial residences hub widely perceived as official; later partnered and handed over."
          },
          {
            "role": "Operator",
            "company": "CopyCat",
            "meta": "Jun 2019–Nov 2022 · Khimki/Moscow, Russia · Venture · Primary",
            "body": "Brand split from iPressa to widen perceived choice with a centralized back office."
          },
          {
            "role": "Founder",
            "company": "iПресса (iPressa)",
            "meta": "Nov 2017–Nov 2022 · Moscow, Russia · Venture · Primary",
            "body": "Zero-to-three offices. Online-first funnel. COVID continuity. Social-commerce ops."
          },
          {
            "role": "Coach & manager",
            "company": "RGAU-MSKHA (gym ops)",
            "meta": "Feb 2017–Nov 2018 · Moscow, Russia · Employment",
            "body": "From coaching to running multi-site facilities; renovation and events."
          },
          {
            "role": "Co-founder",
            "company": "EverBet",
            "meta": "2018 · Moscow, Russia · Experiment",
            "body": "Math-first predictions prototype; shuttered after trials and resourcing review."
          },
          {
            "role": "Agent",
            "company": "Franco Columbu",
            "meta": "Dec 2015–Apr 2017 · Russia/Eastern Europe · Representation",
            "body": "Verified VK presence, translations, community, and press coordination."
          },
          {
            "role": "Experiment lead",
            "company": "Из Дрыща в атлеты",
            "meta": "Jun 2015–Aug 2015 · Moscow, Russia · Experiment",
            "body": "Early media test on transformation under a strict program; ended early."
          }
        ],
        "throughTitle": "Through-line",
        "throughBody": "Orchestrate, ship, hand over. Evidence over adjectives.",
        "contactsTitle": "Contacts"
      },
      "skills": {
        "title": "Artes",
        "sections": [
          {
            "type": "list",
            "heading": "How I operate",
            "items": [
              {"title": "Systems first.", "body": "Map interfaces, constraints, and feedback loops before tasks so decisions line up and rework drops."},
              {"title": "Prioritize hard.", "body": "Protect the critical path and keep WIP low; time-box discovery to force learning over drift."},
              {"title": "Orchestrate.", "body": "Assign clear owners with contracts and acceptance criteria; remove ambiguity fast."},
              {"title": "Write it down.", "body": "Specs, ADRs, runbooks, and post-mortems others can execute without me in the room."},
              {"title": "Ship with guardrails.", "body": "Retries, timeouts, limits, and graceful degradation by default so releases are boring."},
              {"title": "Deterministic handover.", "body": "Leave diagrams, metrics, and ownership transfer that stick."}
            ]
          },
          {
            "type": "list",
            "heading": "Domains I work across",
            "items": [
              {"title": "Software systems & agents.", "body": "Orchestrate agents and services with explicit contracts; evaluate on cost, latency, and accuracy."},
              {"title": "Web product.", "body": "Structure content and UX for clarity; keep payloads thin and releases predictable."},
              {"title": "Research & evidence.", "body": "Design studies, read data sanely, and cite correctly; separate signal from noise."},
              {"title": "Media & visuals.", "body": "Turn ideas into storyboards and assets; edit in DaVinci; shape images in Photoshop."},
              {"title": "Life sciences.", "body": "Translate biology context into product and communication that non-specialists can follow."}
            ]
          },
          {
            "type": "paragraph",
            "heading": "Web builds & small apps",
            "text": "End-to-end delivery from brief to deploy. Clear content, fast performance, predictable releases. Sample artifacts available by email."
          }
        ]
      },
      "education": {
        "title": "Studia",
        "formalTitle": "Formal",
        "formal": [
          {
            "role": "Doctor of Philosophy studies, Biology (withdrew pre-defense)",
            "company": "Russian State Agrarian University – Moscow Timiryazev Agricultural Academy (RGAU-MSKHA)",
            "meta": "Sep 2020–Dec 2023 · Moscow, Russia",
            "body": "What this added: research-ops literacy—study design, lab methods, analysis, and collaboration with senior faculty. Six publications; citations available by email."
          },
          {
            "role": "Master of Science, International Economics and Management",
            "company": "Faculté de Gestion, Economie et Sciences (FGES), Université Catholique de Lille",
            "meta": "Sep 2022–Jul 2023 · Lille, France",
            "body": "Degree awarded. General-management spine and managerial economics. Capstone on managerial adaptation during COVID."
          },
          {
            "role": "Engineer’s program (exchange), Business & Marketing",
            "company": "ISA Lille (JUNIA)",
            "meta": "Sep 2021–Sep 2022 · Lille, France",
            "body": "What this added: engineering-school precision applied to market research, positioning, and agri-food supply chains; French-language practice."
          },
          {
            "role": "Professional program, Cinematography and Film/Video Production",
            "company": "Skillbox (remote)",
            "meta": "Feb 2020–Dec 2022 · Remote",
            "body": "What this added: product imaging and narrative. Storyboards, camera basics, editing workflows in DaVinci Resolve. Applied to ads and product demos."
          },
          {
            "role": "Master’s degree, Agriculture (Genetics)",
            "company": "RGAU-MSKHA",
            "meta": "Sep 2018–Jul 2020 · Moscow, Russia",
            "body": "Animal sciences, aquaculture, agronomy, and environmental systems; quantitative reporting and lab safety."
          },
          {
            "role": "Bachelor’s degree, Agriculture",
            "company": "RGAU-MSKHA",
            "meta": "Sep 2013–Jul 2017 · Moscow, Russia",
            "body": "Foundations in biology, chemistry, genetics, physiology, and production systems."
          }
        ],
        "certTitle": "Certifications & Proficiency",
        "certifications": [
          {
            "role": "TOEIC",
            "company": "975 / 990",
            "meta": "Mar 2023 · Assessment",
            "body": "Advanced professional English proficiency (reading and listening)."
          },
          {
            "role": "Business English courses",
            "company": "RGAU-MSKHA",
            "meta": "2018–2019 · Completed",
            "body": "Academic and professional communication with technical writing and presentations."
          },
          {
            "role": "Certification in Genetics",
            "company": "RGAU with Lomonosov Moscow State University",
            "meta": "2019 · Certificate",
            "body": "Mendelian and molecular genetics, population genetics, lab methods, and data interpretation."
          }
        ]
      }
    },
    "cases": {
      "iz-drysha-v-atlety": {
        "title": "Из Дрыща в атлеты (From a Skinny Kid to an Athlete)",
        "situation": "<strong>Situation.</strong> Early media experiment documenting a fast transformation under strict training.",
        "role": "<strong>Role.</strong> Program design, coaching, and production cadence.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Defined weekly plan for training, nutrition, and recovery.",
          "Planned recurring content to track progress."
        ],
        "outcome": "<strong>Outcome.</strong> Ended early; lesson in scope, pacing, and team pressure.",
        "proofNote": "Proof available by email"
      },
      "rgau-mskha": {
        "title": "Тренажерные залы РГАУ‑МСХА (RGAU-MSKHA Gyms)",
        "situation": "<strong>Situation.</strong> From coaching to managing a distributed university gym network.",
        "role": "<strong>Role.</strong> Coach → manager of gym operations (reporting to a vice-president).",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Planned and executed one full renovation; prepared a second; reopened a third.",
          "Set safety instruction cadence and service add-ons.",
          "Supported campus events and newcomer tours."
        ],
        "outcome": "<strong>Outcome.</strong> Multi-site operations stabilized across up to 8 facilities.",
        "proofNote": "Photos and internal memos available by email"
      },
      "studgorodok-rgau": {
        "title": "Студгородок (Student Residences)",
        "situation": "<strong>Situation.</strong> No official residences channel existed; students needed a trusted hub.",
        "role": "<strong>Role.</strong> Founder/operator; later partner to management.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Launched an unofficial page with clear tone and useful updates.",
          "Coordinated with management and handed operations when adoption grew."
        ],
        "outcome": "<strong>Outcome.</strong> ~4.5k members; page remains active under management.",
        "proofTitle": "<strong>Proof</strong>",
        "proofLinks": ["vk.com/campusrgau"]
      },
      "i-pressa": {
        "title": "iПресса (iPressa)",
        "situation": "<strong>Situation.</strong> Copy/print service from zero with a goal of stable demand and expansion.",
        "role": "<strong>Role.</strong> Founder and operator.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Online-first funnel via VK; early personal fulfillment.",
          "Disciplined reinvestment into capacity.",
          "Scaled to three offices (Jun 2019; Sep/Oct 2019; third site initiated 2020).",
          "COVID continuity plan and standardized SLAs.",
          "Brand separation where useful (CopyCat) with unified back office."
        ],
        "outcome": "<strong>Outcome.</strong> Three locations; daily 30–50 orders (100+ in peaks); ₽500k–700k top-line months; continuity through COVID.",
        "proofTitle": "<strong>Proof</strong>",
        "proofLinks": ["vk.com/i.pressa"],
        "proofNote": "Additional documents available by email"
      },
      "copycat": {
        "title": "Центр полиграфии CopyCat (CopyCat)",
        "situation": "<strong>Situation.</strong> Widen perceived market choice without duplicating operations.",
        "role": "<strong>Role.</strong> Founder/operator.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Split brand from iPressa while keeping a single back office.",
          "Opened a physical site in Khimki to localize acquisition.",
          "Kept standardized pricing and service levels."
        ],
        "outcome": "<strong>Outcome.</strong> Daily tens of orders; lifted engagement in northern Moscow; network effects across brands.",
        "proofTitle": "<strong>Proof</strong>",
        "proofLinks": ["vk.com/copycatprint"]
      },
      "airrods": {
        "title": "AirRods (AirPods Store)",
        "situation": "<strong>Situation.</strong> Instagram-based AirPods storefront serving Moscow with local delivery.",
        "role": "<strong>Role.</strong> Co-creator focused on media, content, and storefront operations.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Shot product photography and short video spots.",
          "Ran Instagram campaigns and DMs for conversion.",
          "Coordinated packaging and last-mile delivery."
        ],
        "outcome": "<strong>Outcome.</strong> Sustained sales; initial investment recovered; account remains visible.",
        "proofTitle": "<strong>Proof</strong>",
        "proofLinks": ["instagram.com/air_rods"]
      },
      "diplosha": {
        "title": "Диплошa (Diplosha)",
        "situation": "<strong>Situation.</strong> Extend existing student work into thesis support.",
        "role": "<strong>Role.</strong> Initiator; recruited domain experts; standardized delivery.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Used VK for intake and communication.",
          "Defined scope, timelines, and acceptance criteria."
        ],
        "outcome": "<strong>Outcome.</strong> 3–4 deliveries; paused due to relocation.",
        "proofTitle": "<strong>Proof</strong>",
        "proofLinks": ["vk.com/diplosha"]
      },
      "franco-columbu": {
        "title": "Franco Columbu",
        "situation": "<strong>Situation.</strong> Representation in Russia/Eastern Europe for a high-profile athlete and author.",
        "role": "<strong>Role.</strong> Personal agent for the region.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Verified official VK presence with content standards.",
          "Managed translations of books and interviews with approvals.",
          "Ran community and coordinated press/product access."
        ],
        "outcome": "<strong>Outcome.</strong> Verified presence, consistent communications, and regional media placements.",
        "proofTitle": "<strong>Proof</strong>",
        "proofLinks": ["vk.com/fcolumbu", "vk.com/francocolumbu"],
        "proofNote": "Additional press on request"
      },
      "everbet": {
        "title": "EverBet",
        "situation": "<strong>Situation.</strong> Short-run experiment in math-driven sports predictions.",
        "role": "<strong>Role.</strong> Co-founder in a 3-person team.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Prototyped models on historical stats.",
          "Set early kill criteria when signal and resources misaligned."
        ],
        "outcome": "<strong>Outcome.</strong> Experiment discontinued after initial trials.",
        "proofTitle": "<strong>Proof</strong>",
        "proofLinks": ["vk.com/everbetmath"]
      },
      "universite-catholique-de-lille": {
        "title": "Université Catholique de Lille",
        "situation": "<strong>Situation.</strong> University teaching and international student support.",
        "role": "<strong>Role.</strong> Lecturer (maître assistant) and program support.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Designed syllabus and assessments for genetics.",
          "Set office-hours cadence and clear communication.",
          "Coordinated exams, grading, and documentation with administration."
        ],
        "outcome": "<strong>Outcome.</strong> Semester delivered. Students assessed. Contract completed.",
        "proofNote": "Syllabus excerpt, screenshots, and photos available by email"
      },
      "euratechnologies": {
        "title": "EuraTechnologies",
        "situation": "<strong>Situation.</strong> Incubation to accelerate inAi. Retail & E-commerce track in Lille.",
        "role": "<strong>Role.</strong> Founder as participant. Aligned venture milestones and customer discovery.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Set a cadence for user interviews and partner outreach.",
          "Define MVP boundaries and “kill criteria.”",
          "Use incubator network for pilots and expert reviews."
        ],
        "outcome": "<strong>Outcome.</strong> Accepted and active since Sep 2025; program artefacts tracked; next stage planned.",
        "proofNote": "Program details available by email"
      },
      "inai": {
        "title": "inAi",
        "situation": "<strong>Situation.</strong> Independent general-purpose AI agent. Built under tight constraints to deliver practical automation.",
        "role": "<strong>Role.</strong> Founder. Product, architecture, delivery, and early GTM. Team of 3. Lille, France.",
        "decisionsTitle": "Decisions",
        "decisions": [
          "Milestone gates with “go/no-go” reviews.",
          "Provider routing and hard cost controls.",
          "Reliability guardrails: timeouts, retries, sane defaults.",
          "Deterministic handover: docs, runbooks, acceptance criteria, and metrics.",
          "Partner lanes for integrations."
        ],
        "outcome": "<strong>Outcome.</strong> Product live; incubation at EuraTechnologies (Sep 2025–present); operating cadence in place.",
        "proofTitle": "<strong>Proof</strong>",
        "proofLinks": ["inai.fr"],
        "proofNote": "EuraTechnologies acceptance available by email"
      }
    }
  }
}

translations["fr"] = {
  "meta": {
    "title": "Empire de Roman",
    "description": "Bienvenue chez Roman et son Empire. Un empire minimaliste et ironique sur une page."
  },
  "hero": {
    "greeting": "Salut.",
    "lead": "Vous pensiez à l'Empire romain.<br>Félicitations. Voici l'Empire de Roman.",
    "block1": "Ce Roman bâtit un empire à travers le monde et les disciplines.<br>Il est vaste et multidimensionnel. Il peut en bâtir un pour vous aussi.",
    "block2": "Ne restons pas coincés dans le passé. Les empires montent et tombent.<br><strong>Mieux vaut essayer {brand}. Ils construisent l'avenir.</strong>",
    "block3": "Si vous voulez quand même voir ce que Roman propose, voici ce que vous obtenez :",
    "block4": "Je transforme des fronts dispersés en une seule campagne qui sort.",
    "block5": "Entreprise multi-sites construite · Enseignant à l'université · Agent et représentation personnelle",
    "btn_try": "Essayer",
    "btn_skills": "Artes",
    "btn_cv": "Cursus Honorum",
    "btn_education": "Studia",
    "btn_aria": {
      "try": "Essayer inAi",
      "skills": "Ouvrir Artes",
      "cv": "Ouvrir Cursus Honorum",
      "education": "Ouvrir Studia"
    },
    "contact_label": "⟨ Propositions et mises en relation ⟩"
  },
  "pillars": {
    "title": "Quatre piliers de l'Empire",
    "items": [
      {"name": "Franco Columbu", "note": "Présence officielle, traductions et opérations presse."},
      {"name": "inAi", "note": "Construction indépendante du concept au produit."},
      {"name": "iPressa", "note": "De zéro à un puis trois sites ; continuité sous contrainte."},
      {"name": "Université Catholique de Lille", "note": "Enseigné et piloté un programme dans une université française."}
    ]
  },
  "showcase": {
    "title": "Histoire de l'Empire",
    "prev": "Précédent",
    "next": "Suivant",
    "region": "Logos de projets"
  },
  "badges": {
    "archived": "Archivé",
    "active": "Actif",
    "outcome": "Construit + incubé"
  },
  "captions": {
    "iz-drysha-v-atlety": "Essai média sur transformation disciplinée ; arrêté après un sprint initial.",
    "franco-columbu": "Agent Russie/Europe de l'Est ; VK vérifié, traductions, communauté, presse.",
    "everbet": "Prototype de prédictions mathématiques ; fermé après essais.",
    "i-pressa": "Impression/copie de zéro à trois sites ; continuité COVID ; social-commerce.",
    "copycat": "Scission de marque pour élargir le choix avec un back-office unique ; site à Khimki.",
    "airrods": "Boutique AirPods sur Instagram ; acquisition média et livraison locale.",
    "rgau-mskha": "Coach → responsable des salles ; huit sites ; rénovations et plan de réouverture.",
    "studgorodok-rgau": "Hub officieux des résidences, repris par la direction ; ~4,5 k membres.",
    "diplosha": "Spin-off d'aide aux mémoires ; 3–4 livraisons ; pause lors d'une relocalisation.",
    "universite-catholique-de-lille": "Chargé de cours en génétique ; cours assuré ; accompagnement des internationaux.",
    "euratechnologies": "Incubation accélérant inAi ; track Retail & E-commerce."
  },
  "inaiSpotlight": {
    "aria": "Ouvrir la fiche inAi"
  },
  "aria": {
    "lang_switcher": "Sélecteur de langue",
    "portrait_alt": "Portrait de Roman Chuikov",
    "portrait_caption": "Portrait de Roman Chuikov",
    "modal_close": "Fermer"
  },
  "modals": {
    "cv": {
      "title": "Cursus Honorum",
      "summary": "Bâtisseur-opérateur sur plusieurs disciplines.<br>Basé en France. Focalisation : inAi.<br>Quand m'engager : audit, lancement, redressement.",
      "campaignsTitle": "Campagnes",
      "campaigns": [
        {
          "role": "Fondateur",
          "company": "inAi",
          "meta": "Juin 2025–présent · Lille, France · Venture · Principal",
          "body": "Agent IA généraliste. Équipe de 3 personnes. Fiabilité, contrôle des coûts et discipline de passation."
        },
        {
          "role": "Participant",
          "company": "EuraTechnologies (incubation)",
          "meta": "Sep 2025–présent · Lille, France · Parcours Retail & E-commerce",
          "body": "Incubation soutenant les jalons d'inAi, la découverte et les canaux partenaires. Preuve disponible par email."
        },
        {
          "role": "Enseignant",
          "company": "Université Catholique de Lille",
          "meta": "Août 2022–sept. 2023 · Lille, France · Emploi",
          "body": "Cours de génétique délivré et accompagnement des programmes internationaux. Supports disponibles sur demande."
        },
        {
          "role": "Co-créateur",
          "company": "AirRods (boutique AirPods)",
          "meta": "Nov 2019–mars 2021 · Moscou, Russie · Venture · Secondaire",
          "body": "Boutique Instagram. Roman pilotait médias, contenus et exécution logistique."
        },
        {
          "role": "Initiateur",
          "company": "Диплошa (Diplosha)",
          "meta": "Mai 2020–juil. 2021 · Moscou, Russie · Venture · Secondaire",
          "body": "Spin-off d'accompagnement de mémoires pour des clients étudiants existants ; pause lors de la relocalisation."
        },
        {
          "role": "Fondateur",
          "company": "Студгородок (Student Residences)",
          "meta": "Nov 2019–avr. 2020 (passation) · Moscou, Russie · Venture · Secondaire",
          "body": "Hub officieux des résidences perçu comme officiel ; partenariat puis passation."
        },
        {
          "role": "Opérateur",
          "company": "CopyCat",
          "meta": "Juin 2019–nov. 2022 · Khimki/Moscou, Russie · Venture · Principal",
          "body": "Marque dissociée d'iPressa pour élargir le choix avec un back-office centralisé."
        },
        {
          "role": "Fondateur",
          "company": "iПресса (iPressa)",
          "meta": "Nov 2017–nov. 2022 · Moscou, Russie · Venture · Principal",
          "body": "Trois sites ouverts. Tunnel en ligne. Continuité COVID. Opérations social-commerce."
        },
        {
          "role": "Coach et manager",
          "company": "RGAU-MSKHA (gestion des salles)",
          "meta": "Fév 2017–nov. 2018 · Moscou, Russie · Emploi",
          "body": "Du coaching à la direction de sites multiples ; rénovations et événements."
        },
        {
          "role": "Co-fondateur",
          "company": "EverBet",
          "meta": "2018 · Moscou, Russie · Expérimentation",
          "body": "Prototype de prédictions mathématiques ; arrêté après essais et revue des ressources."
        },
        {
          "role": "Agent",
          "company": "Franco Columbu",
          "meta": "Déc 2015–avr. 2017 · Russie/Europe de l'Est · Représentation",
          "body": "Présence VK vérifiée, traductions, communauté et coordination presse."
        },
        {
          "role": "Chef d'expérience",
          "company": "Из Дрыща в атлеты",
          "meta": "Juin 2015–août 2015 · Moscou, Russie · Expérimentation",
          "body": "Test média précoce sur une transformation sous programme strict ; interrompu tôt."
        }
      ],
      "throughTitle": "Fil conducteur",
      "throughBody": "Orchestrer, livrer, transmettre. Les preuves avant les adjectifs.",
      "contactsTitle": "Contacts"
    },
    "skills": {
      "title": "Artes",
      "sections": [
        {
          "type": "list",
          "heading": "Comment j'opère",
          "items": [
            {"title": "D'abord les systèmes.", "body": "Cartographier interfaces, contraintes et boucles de retour avant les tâches pour aligner les décisions et réduire les reprises."},
            {"title": "Prioriser sans relâche.", "body": "Protéger le chemin critique et limiter le WIP ; borner l'exploration pour forcer l'apprentissage plutôt que la dérive."},
            {"title": "Orchestrer.", "body": "Assigner des responsables clairs avec contrats et critères d'acceptation ; lever l'ambiguïté rapidement."},
            {"title": "Tout écrire.", "body": "Spécifications, ADR, runbooks et post-mortems que d'autres peuvent exécuter sans moi dans la pièce."},
            {"title": "Livrer avec des garde-fous.", "body": "Relances, timeouts, limites et dégradations maîtrisées par défaut pour des mises en production sans surprise."},
            {"title": "Passation déterministe.", "body": "Laisser des schémas, métriques et transferts de responsabilité qui tiennent."}
          ]
        },
        {
          "type": "list",
          "heading": "Domaines d'intervention",
          "items": [
            {"title": "Systèmes logiciels & agents.", "body": "Orchestrer agents et services avec des contrats explicites ; évaluer coût, latence et précision."},
            {"title": "Produit web.", "body": "Structurer contenu et UX pour la clarté ; maintenir des charges légères et des sorties prévisibles."},
            {"title": "Recherche & preuves.", "body": "Concevoir des études, lire la donnée avec rigueur, citer correctement ; distinguer signal et bruit."},
            {"title": "Médias & visuels.", "body": "Transformer les idées en storyboards et assets ; montage sur DaVinci ; retouches sur Photoshop."},
            {"title": "Sciences de la vie.", "body": "Traduire le contexte biologique en produit et communication accessibles aux non-spécialistes."}
          ]
        },
        {
          "type": "paragraph",
          "heading": "Constructions web & petites apps",
          "text": "Livraison de bout en bout du brief au déploiement. Contenus clairs, performance rapide, sorties prévisibles. Exemples disponibles par email."
        }
      ]
    },
    "education": {
      "title": "Studia",
      "formalTitle": "Parcours académique",
      "formal": [
        {
          "role": "Doctorat de biologie (abandon avant soutenance)",
          "company": "Université agricole d'État de Russie – Académie agricole Timiryazev de Moscou (RGAU-MSKHA)",
          "meta": "Sep 2020–déc 2023 · Moscou, Russie",
          "body": "Apports : maîtrise des opérations de recherche — conception d'études, méthodes de laboratoire, analyses et collaboration avec le corps professoral. Six publications ; références sur demande."
        },
        {
          "role": "Master of Science, Économie et management internationaux",
          "company": "Faculté de Gestion, Economie et Sciences (FGES), Université Catholique de Lille",
          "meta": "Sep 2022–juil. 2023 · Lille, France",
          "body": "Diplôme obtenu. Pilier de management général et économie managériale. Projet final sur l'adaptation managériale pendant le COVID."
        },
        {
          "role": "Programme d'ingénieur (échange), Business & Marketing",
          "company": "ISA Lille (JUNIA)",
          "meta": "Sep 2021–sep 2022 · Lille, France",
          "body": "Apports : rigueur d'école d'ingénieur appliquée aux études de marché, au positionnement et aux chaînes agroalimentaires ; pratique du français."
        },
        {
          "role": "Programme professionnel, Cinématographie et production audiovisuelle",
          "company": "Skillbox (à distance)",
          "meta": "Fév 2020–déc 2022 · À distance",
          "body": "Apports : image produit et narration. Storyboards, bases caméra, flux de montage sur DaVinci Resolve. Utilisés pour pubs et démos produit."
        },
        {
          "role": "Master, Agriculture (génétique)",
          "company": "RGAU-MSKHA",
          "meta": "Sep 2018–juil. 2020 · Moscou, Russie",
          "body": "Sciences animales, aquaculture, agronomie et systèmes environnementaux ; reporting quantitatif et sécurité de laboratoire."
        },
        {
          "role": "Licence, Agriculture",
          "company": "RGAU-MSKHA",
          "meta": "Sep 2013–juil. 2017 · Moscou, Russie",
          "body": "Bases en biologie, chimie, génétique, physiologie et systèmes de production."
        }
      ],
      "certTitle": "Certifications & compétences",
      "certifications": [
        {
          "role": "TOEIC",
          "company": "975 / 990",
          "meta": "Mar 2023 · Certification",
          "body": "Anglais professionnel avancé (compréhension écrite et orale)."
        },
        {
          "role": "Cours d'anglais business",
          "company": "RGAU-MSKHA",
          "meta": "2018–2019 · Validé",
          "body": "Communication académique et professionnelle avec rédaction technique et présentations."
        },
        {
          "role": "Certification en génétique",
          "company": "RGAU avec l'Université d'État de Moscou Lomonossov",
          "meta": "2019 · Certificat",
          "body": "Génétique mendélienne et moléculaire, génétique des populations, méthodes de laboratoire et interprétation des données."
        }
      ]
    }
  },
  "cases": {
    "iz-drysha-v-atlety": {
      "title": "Из Дрыща в атлеты (De gringalet à athlète)",
      "situation": "<strong>Situation.</strong> Expérience média précoce documentant une transformation rapide sous entraînement strict.",
      "role": "<strong>Rôle.</strong> Conception du programme, coaching et cadence de production.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Plan hebdomadaire défini pour l'entraînement, la nutrition et la récupération.",
        "Contenus récurrents planifiés pour mesurer la progression."
      ],
      "outcome": "<strong>Résultat.</strong> Arrêt anticipé ; leçon sur le périmètre, le rythme et la pression d'équipe.",
      "proofNote": "Preuves disponibles par email"
    },
    "rgau-mskha": {
      "title": "Тренажерные залы РГАУ‑МСХА (Salles de sport RGAU-MSKHA)",
      "situation": "<strong>Situation.</strong> Passage du coaching à la gestion d'un réseau universitaire de salles de sport.",
      "role": "<strong>Rôle.</strong> Coach devenu responsable des opérations des salles (reporting vice-président).",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Planification et réalisation d'une rénovation complète ; préparation d'une seconde ; réouverture d'une troisième salle.",
        "Mise en place de cadences de sécurité et d'offres additionnelles.",
        "Soutien aux événements du campus et aux visites des nouveaux."
      ],
      "outcome": "<strong>Résultat.</strong> Exploitation multi-sites stabilisée sur jusqu'à huit installations.",
      "proofNote": "Photos et notes internes disponibles par email"
    },
    "studgorodok-rgau": {
      "title": "Студгородок (Résidences étudiantes)",
      "situation": "<strong>Situation.</strong> Aucun canal officiel pour les résidences ; besoin d'un hub fiable pour les étudiants.",
      "role": "<strong>Rôle.</strong> Fondateur/opérateur ; ensuite partenaire de l'administration.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Page officieuse lancée avec ton clair et informations utiles.",
        "Coordination avec l'administration puis transfert lorsque l'adoption a grandi."
      ],
      "outcome": "<strong>Résultat.</strong> ~4,5 k membres ; page maintenue par la direction.",
      "proofTitle": "<strong>Preuves</strong>",
      "proofLinks": ["vk.com/campusrgau"]
    },
    "i-pressa": {
      "title": "iПресса (iPressa)",
      "situation": "<strong>Situation.</strong> Service d'impression/copie créé de zéro avec objectif de demande stable et expansion.",
      "role": "<strong>Rôle.</strong> Fondateur et opérateur.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Tunnel en ligne via VK ; exécution personnelle au départ.",
        "Réinvestissement discipliné dans la capacité.",
        "Passage à trois sites (juin 2019 ; sep/oct 2019 ; troisième site amorcé en 2020).",
        "Plan de continuité COVID et SLAs standardisés.",
        "Séparation de marque (CopyCat) lorsque utile avec back-office unifié."
      ],
      "outcome": "<strong>Résultat.</strong> Trois implantations ; 30–50 commandes quotidiennes (100+ en pic) ; mois à 500–700 k₽ de CA ; continuité pendant le COVID.",
      "proofTitle": "<strong>Preuves</strong>",
      "proofLinks": ["vk.com/i.pressa"],
      "proofNote": "Documents supplémentaires disponibles par email"
    },
    "copycat": {
      "title": "Центр полиграфии CopyCat (CopyCat)",
      "situation": "<strong>Situation.</strong> Élargir le choix perçu sans dupliquer les opérations.",
      "role": "<strong>Rôle.</strong> Fondateur/opérateur.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Scission d'iPressa tout en conservant un back-office unique.",
        "Ouverture d'un site physique à Khimki pour localiser l'acquisition.",
        "Tarifs et niveaux de service standardisés maintenus."
      ],
      "outcome": "<strong>Résultat.</strong> Plusieurs dizaines de commandes par jour ; engagement renforcé au nord de Moscou ; effets de réseau entre les marques.",
      "proofTitle": "<strong>Preuves</strong>",
      "proofLinks": ["vk.com/copycatprint"]
    },
    "airrods": {
      "title": "AirRods (Boutique AirPods)",
      "situation": "<strong>Situation.</strong> Boutique AirPods sur Instagram desservant Moscou avec livraison locale.",
      "role": "<strong>Rôle.</strong> Co-créateur en charge des médias, du contenu et des opérations.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Prises de vue produits et spots vidéo courts.",
        "Campagnes Instagram et gestion des DM pour convertir.",
        "Coordination emballage et livraison du dernier kilomètre."
      ],
      "outcome": "<strong>Résultat.</strong> Ventes soutenues ; investissement initial remboursé ; compte toujours visible.",
      "proofTitle": "<strong>Preuves</strong>",
      "proofLinks": ["instagram.com/air_rods"]
    },
    "diplosha": {
      "title": "Диплошa (Diplosha)",
      "situation": "<strong>Situation.</strong> Étendre l'accompagnement étudiant existant vers le support de mémoires.",
      "role": "<strong>Rôle.</strong> Initiateur ; recrutement d'experts ; standardisation des livrables.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Utilisation de VK pour l'acquisition et les échanges.",
        "Définition du périmètre, des délais et des critères d'acceptation."
      ],
      "outcome": "<strong>Résultat.</strong> 3–4 livraisons ; pause due à la relocalisation.",
      "proofTitle": "<strong>Preuves</strong>",
      "proofLinks": ["vk.com/diplosha"]
    },
    "franco-columbu": {
      "title": "Franco Columbu",
      "situation": "<strong>Situation.</strong> Représentation en Russie/Europe de l'Est pour un athlète et auteur de premier plan.",
      "role": "<strong>Rôle.</strong> Agent personnel pour la région.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Présence officielle VK vérifiée avec standards éditoriaux.",
        "Gestion des traductions d'ouvrages et d'interviews avec validations.",
        "Animation de la communauté et coordination presse/produits."
      ],
      "outcome": "<strong>Résultat.</strong> Présence vérifiée, communications cohérentes et retombées médias régionales.",
      "proofTitle": "<strong>Preuves</strong>",
      "proofLinks": ["vk.com/fcolumbu", "vk.com/francocolumbu"],
      "proofNote": "Presse supplémentaire sur demande"
    },
    "everbet": {
      "title": "EverBet",
      "situation": "<strong>Situation.</strong> Expérimentation courte de prédictions sportives basées sur les maths.",
      "role": "<strong>Rôle.</strong> Co-fondateur dans une équipe de 3 personnes.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Prototypage de modèles sur statistiques historiques.",
        "Définition de critères d'arrêt anticipé quand le signal ne suivait pas les ressources."
      ],
      "outcome": "<strong>Résultat.</strong> Expérimentation arrêtée après les premiers essais.",
      "proofTitle": "<strong>Preuves</strong>",
      "proofLinks": ["vk.com/everbetmath"]
    },
    "universite-catholique-de-lille": {
      "title": "Université Catholique de Lille",
      "situation": "<strong>Situation.</strong> Enseignement universitaire et accompagnement des étudiants internationaux.",
      "role": "<strong>Rôle.</strong> Enseignant (maître-assistant) et support de programme.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Conception du syllabus et des évaluations en génétique.",
        "Mise en place de permanences et de communications claires.",
        "Coordination examens, notations et dossiers avec l'administration."
      ],
      "outcome": "<strong>Résultat.</strong> Semestre délivré. Étudiants évalués. Contrat terminé.",
      "proofNote": "Extraits de syllabus, captures et photos disponibles par email"
    },
    "euratechnologies": {
      "title": "EuraTechnologies",
      "situation": "<strong>Situation.</strong> Incubation pour accélérer inAi sur le track Retail & E-commerce à Lille.",
      "role": "<strong>Rôle.</strong> Fondateur participant. Alignement des jalons venture et de la découverte client.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Cadence fixée pour les entretiens utilisateurs et la prospection partenaires.",
        "Définition des limites MVP et des critères d'arrêt.",
        "Utilisation du réseau de l'incubateur pour pilotes et revues expertes."
      ],
      "outcome": "<strong>Résultat.</strong> Accepté et actif depuis sept. 2025 ; artefacts suivis ; prochaine étape planifiée.",
      "proofNote": "Détails du programme disponibles par email"
    },
    "inai": {
      "title": "inAi",
      "situation": "<strong>Situation.</strong> Agent IA généraliste indépendant. Construit sous fortes contraintes pour automatiser concrètement.",
      "role": "<strong>Rôle.</strong> Fondateur. Produit, architecture, delivery et early GTM. Équipe de 3. Lille, France.",
      "decisionsTitle": "Décisions",
      "decisions": [
        "Gates de jalons avec revues go/no-go.",
        "Routage fournisseurs et contrôle strict des coûts.",
        "Garde-fous de fiabilité : timeouts, retries, défauts sains.",
        "Passation déterministe : docs, runbooks, critères d'acceptation et métriques.",
        "Voies partenaires pour les intégrations."
      ],
      "outcome": "<strong>Résultat.</strong> Produit en ligne ; incubation à EuraTechnologies (sept. 2025–présent) ; cadence opérationnelle en place.",
      "proofTitle": "<strong>Preuves</strong>",
      "proofLinks": ["inai.fr"],
      "proofNote": "Lettre d'acceptation EuraTechnologies disponible par email"
    }
  }
}

translations["ru"] = {
  "meta": {
    "title": "Империя Романа",
    "description": "Добро пожаловать к Роману и его Империи. Минималистичная и ироничная одностраничная империя."
  },
  "hero": {
    "greeting": "Привет.",
    "lead": "Думали о Римской империи — нашли Империю Романа.",
    "block1": "Этот Роман строит империю по миру и в разных дисциплинах.<br>Она широкая и многомерная. Он может построить такую и для вас.",
    "block2": "Но в прошлом зависать не будем. Империи растут и падают.<br><strong>Лучше зайти на {brand}. Они строят будущее.</strong>",
    "block3": "Если всё же хотите узнать, что делает Роман, вот что вы получите:",
    "block4": "Свожу разрозненные фронты в одну кампанию, которая выходит в прод.",
    "block5": "Построил сеть из нескольких точек · Преподаватель в университете · Личный агент и представительство",
    "btn_try": "Попробовать",
    "btn_skills": "Artes",
    "btn_cv": "Cursus Honorum",
    "btn_education": "Studia",
    "btn_aria": {
      "try": "Попробовать inAi",
      "skills": "Открыть Artes",
      "cv": "Открыть Cursus Honorum",
      "education": "Открыть Studia"
    },
    "contact_label": "⟨ Предложения и знакомства ⟩"
  },
  "pillars": {
    "title": "Четыре столпа Империи",
    "items": [
      {"name": "Франко Коломбу", "note": "Официальное присутствие, переводы и работа с прессой."},
      {"name": "inAi", "note": "От концепта до продукта — самостоятельно."},
      {"name": "iPressa", "note": "От нуля до трёх точек; устойчивость под нагрузкой."},
      {"name": "Католический университет Лилля", "note": "Преподавал и вёл программу во французском университете."}
    ]
  },
  "showcase": {
    "title": "История Империи",
    "prev": "Назад",
    "next": "Вперёд",
    "region": "Логотипы проектов"
  },
  "badges": {
    "archived": "Архив",
    "active": "Активно",
    "outcome": "Сделано + инкубируется"
  },
  "captions": {
    "iz-drysha-v-atlety": "Ранний медиапроект о дисциплинированной трансформации; завершён после первого спринта.",
    "franco-columbu": "Агент в России/Восточной Европе; верифицированный VK, переводы, сообщество, пресса.",
    "everbet": "Короткий прототип математических прогнозов; закрыт после испытаний.",
    "i-pressa": "Типография/копи-центр: с нуля до трёх офисов; план непрерывности в COVID; social-commerce операции.",
    "copycat": "Разделение бренда для расширения выбора при едином бэк-офисе; офлайн-точка в Химках.",
    "airrods": "Магазин AirPods в Instagram; лидогенерация через контент и локальная доставка.",
    "rgau-mskha": "Тренер → менеджер залов; восемь площадок; ремонт и план перезапуска.",
    "studgorodok-rgau": "Неофициальный хаб общежитий, принятый администрацией; ~4,5 тыс. участников.",
    "diplosha": "Спин-офф поддержки дипломов; 3–4 выполненных заказа; пауза из-за релокации.",
    "universite-catholique-de-lille": "Преподаватель генетики; курс проведён; поддержка иностранных студентов.",
    "euratechnologies": "Инкубация для ускорения inAi; трек Retail & E-commerce."
  },
  "inaiSpotlight": {
    "aria": "Открыть кейс inAi"
  },
  "aria": {
    "lang_switcher": "Переключатель языка",
    "portrait_alt": "Портрет Романа Чуйкова",
    "portrait_caption": "Портрет Романа Чуйкова",
    "modal_close": "Закрыть"
  },
  "modals": {
    "cv": {
      "title": "Cursus Honorum",
      "summary": "Строитель-оператор в нескольких дисциплинах.<br>Базируюсь во Франции. Фокус: inAi.<br>Когда привлекать: аудит, запуск, спасение.",
      "campaignsTitle": "Кампании",
      "campaigns": [
        {
          "role": "Основатель",
          "company": "inAi",
          "meta": "Июн 2025–по н.в. · Лилль, Франция · Венчур · Основной",
          "body": "Универсальный ИИ-агент. Команда из 3 человек. Надёжность, контроль затрат и дисциплина передачи."
        },
        {
          "role": "Участник",
          "company": "EuraTechnologies (инкьюбация)",
          "meta": "Сен 2025–по н.в. · Лилль, Франция · Трек Retail & E-commerce",
          "body": "Инкубация поддерживает вехи inAi, исследования и партнёрские каналы. Подтверждения по email."
        },
        {
          "role": "Преподаватель",
          "company": "Католический университет Лилля",
          "meta": "Авг 2022–сен 2023 · Лилль, Франция · Работа",
          "body": "Вёл курс по генетике и помог международным программам. Материалы по запросу."
        },
        {
          "role": "Соавтор",
          "company": "AirRods (магазин AirPods)",
          "meta": "Ноя 2019–мар 2021 · Москва, Россия · Венчур · Сторона",
          "body": "Магазин в Instagram. Роман отвечал за медиа, контент и операционное исполнение."
        },
        {
          "role": "Инициатор",
          "company": "Диплошa (Diplosha)",
          "meta": "Май 2020–июл 2021 · Москва, Россия · Венчур · Сторона",
          "body": "Спин-офф помощи с дипломами для существующих студентов; пауза из-за релокации."
        },
        {
          "role": "Основатель",
          "company": "Студгородок (Student Residences)",
          "meta": "Ноя 2019–апр 2020 (передача) · Москва, Россия · Венчур · Сторона",
          "body": "Неофициальный хаб общежитий, который приняли как официальный; позже партнёрство и передача."
        },
        {
          "role": "Оператор",
          "company": "CopyCat",
          "meta": "Июн 2019–ноя 2022 · Химки/Москва, Россия · Венчур · Основной",
          "body": "Отделение бренда от iPressa, чтобы расширить выбор при едином бэк-офисе."
        },
        {
          "role": "Основатель",
          "company": "iПресса (iPressa)",
          "meta": "Ноя 2017–ноя 2022 · Москва, Россия · Венчур · Основной",
          "body": "Сеть из трёх точек. Онлайн-воронка. План непрерывности в COVID. Social-commerce."
        },
        {
          "role": "Тренер и управляющий",
          "company": "РГАУ‑МСХА (спортзалы)",
          "meta": "Фев 2017–ноя 2018 · Москва, Россия · Работа",
          "body": "От тренерства до управления сетью залов; ремонты и события."
        },
        {
          "role": "Сооснователь",
          "company": "EverBet",
          "meta": "2018 · Москва, Россия · Эксперимент",
          "body": "Прототип математических прогнозов; закрыт после тестов и оценки ресурсов."
        },
        {
          "role": "Агент",
          "company": "Franco Columbu",
          "meta": "Дек 2015–апр 2017 · Россия/Восточная Европа · Представительство",
          "body": "Официальный VK, переводы, сообщество и координация прессы."
        },
        {
          "role": "Руководитель эксперимента",
          "company": "Из Дрыща в атлеты",
          "meta": "Июн 2015–авг 2015 · Москва, Россия · Эксперимент",
          "body": "Ранний медиатест трансформации по строгой программе; завершён досрочно."
        }
      ],
      "throughTitle": "Принцип",
      "throughBody": "Оркестровать, запускать, передавать. Факты важнее эпитетов.",
      "contactsTitle": "Контакты"
    },
    "skills": {
      "title": "Artes",
      "sections": [
        {
          "type": "list",
          "heading": "Как я работаю",
          "items": [
            {"title": "Сначала система.", "body": "Определяю интерфейсы, ограничения и петли обратной связи до задач, чтобы решения выстраивались и не было переделок."},
            {"title": "Жёстко приоритезирую.", "body": "Защищаю критический путь и держу низкий WIP; лимитирую исследование, чтобы ускорять обучение."},
            {"title": "Оркеструю.", "body": "Назначаю понятных ответственных с контрактами и критериями приёмки; быстро убираю неоднозначность."},
            {"title": "Документирую.", "body": "Спеки, ADR, runbook и разборы, которые можно выполнять без моего присутствия."},
            {"title": "Релизы с ограничителями.", "body": "Повторы, таймауты, лимиты и управляемая деградация по умолчанию — чтобы релизы были спокойными."},
            {"title": "Контролируемая передача.", "body": "Оставляю схемы, метрики и передачу ответственности, которые держатся."}
          ]
        },
        {
          "type": "list",
          "heading": "Области работы",
          "items": [
            {"title": "Программные системы и агенты.", "body": "Оркеструю агенты и сервисы с явными контрактами; оцениваю стоимость, задержки и точность."},
            {"title": "Веб-продукт.", "body": "Структурирую контент и UX для ясности; держу нагрузку лёгкой и релизы предсказуемыми."},
            {"title": "Исследования и доказательства.", "body": "Проектирую исследования, читаю данные без искажений, корректно цитирую; отделяю сигнал от шума."},
            {"title": "Медиа и визуал.", "body": "Перевожу идеи в раскадровки и ассеты; монтирую в DaVinci; работаю с графикой в Photoshop."},
            {"title": "Бионауки.", "body": "Перевожу биологический контекст в продукт и коммуникацию, понятные неспециалистам."}
          ]
        },
        {
          "type": "paragraph",
          "heading": "Веб-проекты и мини-приложения",
          "text": "Полный цикл от запроса до релиза. Чёткий контент, быстрая работа, предсказуемые запуски. Примеры артефактов — по email."
        }
      ]
    },
    "education": {
      "title": "Studia",
      "formalTitle": "Формальное образование",
      "formal": [
        {
          "role": "Аспирантура по биологии (ушёл до защиты)",
          "company": "Российский государственный аграрный университет – Московская сельскохозяйственная академия им. Тимирязева (РГАУ‑МСХА)",
          "meta": "Сен 2020–дек 2023 · Москва, Россия",
          "body": "Что дала: грамотность в исследовательских операциях — дизайн исследований, лабораторные методы, анализ и работа с профессорами. Шесть публикаций; ссылки по запросу."
        },
        {
          "role": "Master of Science, Международная экономика и менеджмент",
          "company": "FGES, Университет Католический де Лилль",
          "meta": "Сен 2022–июл 2023 · Лилль, Франция",
          "body": "Диплом получен. Каркас общего менеджмента и управленческая экономика. Финальный проект об адаптации менеджеров во время COVID."
        },
        {
          "role": "Инженерная программа (обмен), Business & Marketing",
          "company": "ISA Lille (JUNIA)",
          "meta": "Сен 2021–сен 2022 · Лилль, Франция",
          "body": "Точность инженерной школы применена к исследованиям рынка, позиционированию и агропищевым цепочкам; практика французского."
        },
        {
          "role": "Профессиональная программа, Кинематография и видеопродакшн",
          "company": "Skillbox (дистанционно)",
          "meta": "Фев 2020–дек 2022 · Удалённо",
          "body": "Что дала: визуал продукта и история. Раскадровки, основы камеры, монтаж в DaVinci Resolve. Применено к рекламе и демо."
        },
        {
          "role": "Магистратура, Сельское хозяйство (генетика)",
          "company": "РГАУ‑МСХА",
          "meta": "Сен 2018–июл 2020 · Москва, Россия",
          "body": "Животноводство, аквакультура, агрономия и экосистемы; количественные отчёты и безопасность в лаборатории."
        },
        {
          "role": "Бакалавриат, Сельское хозяйство",
          "company": "РГАУ‑МСХА",
          "meta": "Сен 2013–июл 2017 · Москва, Россия",
          "body": "Базы по биологии, химии, генетике, физиологии и производственным системам."
        }
      ],
      "certTitle": "Сертификаты и уровень",
      "certifications": [
        {
          "role": "TOEIC",
          "company": "975 / 990",
          "meta": "Мар 2023 · Экзамен",
          "body": "Продвинутый профессиональный английский (аудирование и чтение)."
        },
        {
          "role": "Курсы делового английского",
          "company": "РГАУ‑МСХА",
          "meta": "2018–2019 · Завершено",
          "body": "Академическая и деловая коммуникация с техническим письмом и презентациями."
        },
        {
          "role": "Сертификат по генетике",
          "company": "РГАУ совместно с МГУ им. Ломоносова",
          "meta": "2019 · Сертификат",
          "body": "Менделевская и молекулярная генетика, генетика популяций, лабораторные методы и интерпретация данных."
        }
      ]
    }
  },
  "cases": {
    "iz-drysha-v-atlety": {
      "title": "Из Дрыща в атлеты (из худого в атлета)",
      "situation": "<strong>Ситуация.</strong> Ранний медиапроект о быстрой трансформации под жёсткий тренировочный режим.",
      "role": "<strong>Роль.</strong> Программа, тренинг и темп продакшена.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Составил еженедельный план тренинга, питания и восстановления.",
        "Запланировал регулярный контент для фиксации прогресса."
      ],
      "outcome": "<strong>Результат.</strong> Проект завершён досрочно; урок о масштабе, темпе и командном давлении.",
      "proofNote": "Подтверждения по email"
    },
    "rgau-mskha": {
      "title": "Тренажерные залы РГАУ‑МСХА",
      "situation": "<strong>Ситуация.</strong> От тренерства к управлению распределённой сетью университетских залов.",
      "role": "<strong>Роль.</strong> Тренер → менеджер залов (подотчётность проректору).",
      "decisionsTitle": "Решения",
      "decisions": [
        "Спланировал и провёл одну полную реконструкцию; подготовил вторую; вновь открыл третью площадку.",
        "Настроил регламенты по безопасности и дополнительные услуги.",
        "Поддерживал события кампуса и экскурсии для новичков."
      ],
      "outcome": "<strong>Результат.</strong> Стабилизировал мульти-сайтовые операции на восьми площадках.",
      "proofNote": "Фото и внутренние записки по email"
    },
    "studgorodok-rgau": {
      "title": "Студгородок (общежития)",
      "situation": "<strong>Ситуация.</strong> Не было официального канала общежитий; студентам нужен был надёжный центр.",
      "role": "<strong>Роль.</strong> Основатель/оператор; позже партнёр администрации.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Запустил неофициальную страницу с понятным тоном и полезными обновлениями.",
        "Скоординировал передачу с администрацией, когда аудитория выросла."
      ],
      "outcome": "<strong>Результат.</strong> ~4,5 тыс. участников; страница ведётся администрацией.",
      "proofTitle": "<strong>Доказательства</strong>",
      "proofLinks": ["vk.com/campusrgau"]
    },
    "i-pressa": {
      "title": "iПресса (iPressa)",
      "situation": "<strong>Ситуация.</strong> Запуск копировального сервиса с нуля с целью стабильного спроса и роста.",
      "role": "<strong>Роль.</strong> Основатель и оператор.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Онлайн-воронка через VK; на старте — личное исполнение заказов.",
        "Дисциплинированное реинвестирование в мощность.",
        "Масштабирование до трёх точек (июн 2019; сен/окт 2019; третья запущена в 2020).",
        "План непрерывности в COVID и стандартизированные SLA.",
        "Разветвление бренда (CopyCat) при едином бэк-офисе, когда это полезно."
      ],
      "outcome": "<strong>Результат.</strong> Три локации; 30–50 заказов в день (100+ в пики); выручка 500–700 тыс. ₽ в месяц; пережили COVID.",
      "proofTitle": "<strong>Доказательства</strong>",
      "proofLinks": ["vk.com/i.pressa"],
      "proofNote": "Дополнительные документы по email"
    },
    "copycat": {
      "title": "Центр полиграфии CopyCat (CopyCat)",
      "situation": "<strong>Ситуация.</strong> Расширить выбор на рынке без удвоения операций.",
      "role": "<strong>Роль.</strong> Основатель/оператор.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Отделил бренд от iPressa, сохранив единый бэк-офис.",
        "Открыл офлайн-точку в Химках для локального привлечения.",
        "Сохранил стандартизированные цены и уровень сервиса."
      ],
      "outcome": "<strong>Результат.</strong> Десятки заказов ежедневно; рост вовлечения на севере Москвы; сетевые эффекты между брендами.",
      "proofTitle": "<strong>Доказательства</strong>",
      "proofLinks": ["vk.com/copycatprint"]
    },
    "airrods": {
      "title": "AirRods (магазин AirPods)",
      "situation": "<strong>Ситуация.</strong> Instagram-магазин AirPods с доставкой по Москве.",
      "role": "<strong>Роль.</strong> Сооснователь, отвечающий за медиа, контент и операции магазина.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Снимал продуктовые фото и короткие видео.",
        "Вёл кампании в Instagram и переписку в DM для конверсий.",
        "Координировал упаковку и последнюю милю."
      ],
      "outcome": "<strong>Результат.</strong> Стабильные продажи; инвестиции отбиты; аккаунт виден.",
      "proofTitle": "<strong>Доказательства</strong>",
      "proofLinks": ["instagram.com/air_rods"]
    },
    "diplosha": {
      "title": "Диплошa (Diplosha)",
      "situation": "<strong>Ситуация.</strong> Расширить помощь студентам до поддержки дипломов.",
      "role": "<strong>Роль.</strong> Инициатор; привлёк экспертов и стандартизировал выполнение.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Использовал VK для входа и коммуникации.",
        "Определил объём, сроки и критерии приёмки."
      ],
      "outcome": "<strong>Результат.</strong> 3–4 выполненных заказа; пауза из-за релокации.",
      "proofTitle": "<strong>Доказательства</strong>",
      "proofLinks": ["vk.com/diplosha"]
    },
    "franco-columbu": {
      "title": "Franco Columbu",
      "situation": "<strong>Ситуация.</strong> Представительство в России/Восточной Европе для известного атлета и автора.",
      "role": "<strong>Роль.</strong> Личный агент по региону.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Подтвердил официальный VK с контентными стандартами.",
        "Организовал переводы книг и интервью с согласованиями.",
        "Вёл сообщество и координировал доступ прессы и продуктов."
      ],
      "outcome": "<strong>Результат.</strong> Подтверждённое присутствие, стабильные коммуникации и региональные публикации.",
      "proofTitle": "<strong>Доказательства</strong>",
      "proofLinks": ["vk.com/fcolumbu", "vk.com/francocolumbu"],
      "proofNote": "Дополнительная пресса по запросу"
    },
    "everbet": {
      "title": "EverBet",
      "situation": "<strong>Ситуация.</strong> Короткий эксперимент с математическими спортивными прогнозами.",
      "role": "<strong>Роль.</strong> Сооснователь в команде из трёх.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Прототипировали модели на исторической статистике.",
        "Задали ранние критерии остановки при рассинхроне сигнала и ресурсов."
      ],
      "outcome": "<strong>Результат.</strong> Эксперимент закрыт после первых тестов.",
      "proofTitle": "<strong>Доказательства</strong>",
      "proofLinks": ["vk.com/everbetmath"]
    },
    "universite-catholique-de-lille": {
      "title": "Université Catholique de Lille",
      "situation": "<strong>Ситуация.</strong> Университетское преподавание и поддержка иностранных студентов.",
      "role": "<strong>Роль.</strong> Преподаватель (maître assistant) и куратор программы.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Разработал программу и оценивание по генетике.",
        "Настроил график консультаций и прозрачную коммуникацию.",
        "Скоординировал экзамены, оценки и документы с администрацией."
      ],
      "outcome": "<strong>Результат.</strong> Семестр проведён. Студенты оценены. Контракт завершён.",
      "proofNote": "Фрагменты силлабуса, скриншоты и фото — по email"
    },
    "euratechnologies": {
      "title": "EuraTechnologies",
      "situation": "<strong>Ситуация.</strong> Инкубация для ускорения inAi на треке Retail & E-commerce в Лилле.",
      "role": "<strong>Роль.</strong> Основатель-участник. Согласовал венчурные вехи и custdev.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Задал ритм интервью с пользователями и партнёрских контактов.",
        "Определил границы MVP и критерии остановки.",
        "Использовал сеть инкубатора для пилотов и экспертных ревью."
      ],
      "outcome": "<strong>Результат.</strong> В программе с сентября 2025; артефакты фиксируются; следующий этап запланирован.",
      "proofNote": "Детали программы по email"
    },
    "inai": {
      "title": "inAi",
      "situation": "<strong>Ситуация.</strong> Независимый универсальный ИИ-агент. Собран под жёсткие ограничения ради прикладной автоматизации.",
      "role": "<strong>Роль.</strong> Основатель. Продукт, архитектура, доставка и ранний GTM. Команда из 3. Лилль, Франция.",
      "decisionsTitle": "Решения",
      "decisions": [
        "Вехи с ревью go/no-go.",
        "Маршрутизация поставщиков и жёсткий контроль затрат.",
        "Гарантии надёжности: таймауты, повторы, безопасные дефолты.",
        "Детерминированная передача: документы, runbook, критерии приёмки и метрики.",
        "Партнёрские каналы для интеграций."
      ],
      "outcome": "<strong>Результат.</strong> Продукт в запуске; инкубация в EuraTechnologies (сен 2025–н.в.); операционный ритм выстроен.",
      "proofTitle": "<strong>Доказательства</strong>",
      "proofLinks": ["inai.fr"],
      "proofNote": "Письмо о принятии в EuraTechnologies по email"
    }
  }
}

JS_TEMPLATE = """(function(){
  "use strict";

  const translations = %(translations)s;
  const defaultLang = "en";
  const storageKey = "romanempire-lang";
  const langBtns = document.querySelectorAll(".lang-btn");

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
    }catch(err){}
  }

  function detectLanguage(){
    const stored = safeGet(storageKey);
    if(stored && translations[stored]) return stored;
    const browser = navigator.language ? navigator.language.split("-")[0] : "";
    if(browser && translations[browser]) return browser;
    return defaultLang;
  }

  let currentLang = detectLanguage();

  function formatValue(value){
    if(typeof value === "string" && value.indexOf('{brand}') !== -1){
      return value.replace('{brand}', '<span class="brand">in<span class="A">A</span>i.fr</span>');
    }
    return value == null ? "" : value;
  }

  function setHTML(el, value){
    if(!el) return;
    el.innerHTML = formatValue(value);
  }

  function setText(el, value){
    if(!el) return;
    el.textContent = formatValue(value);
  }

  function fillCv(scope, data){
    if(!scope || !data) return;
    setText(scope.querySelector("h3"), data.title);
    setHTML(scope.querySelector(".modal-summary p"), data.summary);

    const campaignsSection = scope.querySelector(".case-body > section.timeline");
    if(campaignsSection){
      setText(campaignsSection.querySelector("h4"), data.campaignsTitle);
      const items = Array.from(campaignsSection.querySelectorAll("ol > li"));
      (data.campaigns || []).forEach(function(entry, idx){
        const li = items[idx];
        if(!li) return;
        setText(li.querySelector(".t-role"), entry.role);
        setText(li.querySelector(".t-company"), entry.company);
        setText(li.querySelector(".t-meta"), entry.meta);
        setText(li.querySelector(".t-body"), entry.body);
      });
    }

    const throughSection = scope.querySelector(".modal-declaration");
    if(throughSection){
      setText(throughSection.querySelector("h4"), data.throughTitle);
      setText(throughSection.querySelector("p"), data.throughBody);
    }

    const contactSection = scope.querySelector(".case-body > section:last-of-type");
    if(contactSection){
      setText(contactSection.querySelector("h4"), data.contactsTitle);
    }
  }

  function fillSkills(scope, data){
    if(!scope || !data) return;
    setText(scope.querySelector("h3"), data.title);
    const sections = Array.from(scope.querySelectorAll(".case-body > section"));
    (data.sections || []).forEach(function(sectionData, idx){
      const sectionEl = sections[idx];
      if(!sectionEl) return;
      setText(sectionEl.querySelector("h4"), sectionData.heading);
      if(sectionData.type === "list"){
        const list = sectionEl.querySelector("ul");
        if(list){
          list.innerHTML = "";
          (sectionData.items || []).forEach(function(item){
            const li = document.createElement("li");
            const strong = document.createElement("strong");
            strong.textContent = item.title;
            li.appendChild(strong);
            li.appendChild(document.createTextNode(" " + item.body));
            list.appendChild(li);
          });
        }
      }else if(sectionData.type === "paragraph"){
        const p = sectionEl.querySelector("p");
        if(p) p.textContent = sectionData.text || "";
      }
    });
  }

  function fillEducation(scope, data){
    if(!scope || !data) return;
    setText(scope.querySelector("h3"), data.title);
    const sections = Array.from(scope.querySelectorAll(".case-body > section.timeline"));
    const formalSection = sections[0];
    if(formalSection){
      setText(formalSection.querySelector("h4"), data.formalTitle);
      const items = Array.from(formalSection.querySelectorAll("ol > li"));
      (data.formal || []).forEach(function(entry, idx){
        const li = items[idx];
        if(!li) return;
        setText(li.querySelector(".t-role"), entry.role);
        setText(li.querySelector(".t-company"), entry.company);
        setText(li.querySelector(".t-meta"), entry.meta);
        setText(li.querySelector(".t-body"), entry.body);
      });
    }
    const certSection = sections[1];
    if(certSection){
      setText(certSection.querySelector("h4"), data.certTitle);
      const items = Array.from(certSection.querySelectorAll("ol > li"));
      (data.certifications || []).forEach(function(entry, idx){
        const li = items[idx];
        if(!li) return;
        setText(li.querySelector(".t-role"), entry.role);
        setText(li.querySelector(".t-company"), entry.company);
        setText(li.querySelector(".t-meta"), entry.meta);
        setText(li.querySelector(".t-body"), entry.body);
      });
    }
  }

  function fillCase(scope, data){
    if(!scope || !data) return;
    setText(scope.querySelector("h3"), data.title);
    const body = scope.querySelector(".case-body");
    if(!body) return;
    const paragraphs = Array.from(body.children).filter(function(node){ return node.tagName === "P"; });
    if(paragraphs[0]) setHTML(paragraphs[0], data.situation);
    if(paragraphs[1]) setHTML(paragraphs[1], data.role);
    if(paragraphs[2]) setHTML(paragraphs[2], data.outcome);

    const decisionsHeading = body.querySelector("h4");
    if(decisionsHeading) setText(decisionsHeading, data.decisionsTitle);

    const list = body.querySelector("ul");
    if(list){
      list.innerHTML = "";
      (data.decisions || []).forEach(function(text){
        const li = document.createElement("li");
        li.textContent = text;
        list.appendChild(li);
      });
    }

    if(paragraphs[3]){
      if(data.proofTitle){
        setHTML(paragraphs[3], data.proofTitle);
        paragraphs[3].hidden = false;
      }else{
        paragraphs[3].hidden = true;
      }
    }

    const proofLinks = body.querySelector(".proof-links");
    if(proofLinks){
      const linkEls = Array.from(proofLinks.querySelectorAll("a"));
      (data.proofLinks || []).forEach(function(label, idx){
        if(linkEls[idx]) linkEls[idx].textContent = label;
      });
    }

    const note = body.querySelector(".proof-note");
    if(note){
      if(data.proofNote){
        note.textContent = data.proofNote;
        note.hidden = false;
      }else{
        note.textContent = "";
        note.hidden = true;
      }
    }
  }

  const modalFillers = { cv: fillCv, skills: fillSkills, education: fillEducation };
  const caseSlugs = Object.keys((translations.en && translations.en.cases) || {});

  function updateTemplates(lang){
    const data = translations[lang] || translations[defaultLang];
    if(!data) return;
    Object.keys(modalFillers).forEach(function(slug){
      const tpl = document.getElementById('tpl-' + slug);
      if(tpl){
        modalFillers[slug](tpl.content, data.modals && data.modals[slug]);
      }
    });
    caseSlugs.forEach(function(slug){
      const tpl = document.getElementById('tpl-' + slug);
      if(!tpl) return;
      const caseData = data.cases && data.cases[slug];
      if(caseData) fillCase(tpl.content, caseData);
    });
  }

  function setBadgeText(card, selector, text){
    const badge = card.querySelector(selector);
    if(badge) badge.textContent = text || "";
  }

  function applyBaseTranslations(){
    const data = translations[currentLang] || translations[defaultLang];
    if(!data) return;

    const metaTitle = data.meta && data.meta.title || "";
    const metaDesc = data.meta && data.meta.description || "";
    document.title = metaTitle;
    function setMeta(selector, attr, value){
      const el = document.querySelector(selector);
      if(el && value !== undefined) el.setAttribute(attr, value);
    }
    setMeta("meta[name='description']", "content", metaDesc);
    setMeta("meta[property='og:title']", "content", metaTitle);
    setMeta("meta[property='og:description']", "content", metaDesc);
    setMeta("meta[name='twitter:title']", "content", metaTitle);
    setMeta("meta[name='twitter:description']", "content", metaDesc);

    setText(document.querySelector('.hero h1'), data.hero && data.hero.greeting);
    setHTML(document.querySelector('.lead'), data.hero && data.hero.lead);

    const blocks = document.querySelectorAll('.hero .block');
    const blockKeys = ['block1','block2','block3','block4','block5'];
    blockKeys.forEach(function(key, idx){
      const block = blocks[idx];
      if(!block) return;
      if(idx < 3) setHTML(block, data.hero && data.hero[key]);
      else setText(block, data.hero && data.hero[key]);
    });

    const primaryBtn = document.querySelector('.btn');
    if(primaryBtn){
      const text = data.hero && data.hero.btn_try || '';
      const brandSpan = primaryBtn.querySelector('.btn-brand');
      if(brandSpan){
        let textNode = Array.from(primaryBtn.childNodes).find(function(node){ return node.nodeType === Node.TEXT_NODE; });
        if(!textNode){
          textNode = document.createTextNode('');
          primaryBtn.insertBefore(textNode, brandSpan);
        }
        textNode.textContent = text ? text + ' ' : '';
      }else{
        primaryBtn.textContent = text;
      }
      const ariaTry = data.hero && data.hero.btn_aria && data.hero.btn_aria.try;
      primaryBtn.setAttribute('aria-label', ariaTry || text);
    }

    const ghostBtns = document.querySelectorAll('.btn-ghost');
    const ghostMap = [
      { key: 'btn_skills', aria: 'skills' },
      { key: 'btn_cv', aria: 'cv' },
      { key: 'btn_education', aria: 'education' }
    ];
    ghostBtns.forEach(function(btn, idx){
      const mapping = ghostMap[idx];
      if(!mapping) return;
      setText(btn, data.hero && data.hero[mapping.key]);
      const ariaValue = data.hero && data.hero.btn_aria && data.hero.btn_aria[mapping.aria];
      if(ariaValue) btn.setAttribute('aria-label', ariaValue);
    });

    setText(document.querySelector('.contact-label'), data.hero && data.hero.contact_label);

    setText(document.querySelector('.pillars .section-title'), data.pillars && data.pillars.title);
    const pillarButtons = document.querySelectorAll('.pillars .pillar');
    const pillarItems = data.pillars && data.pillars.items || [];
    pillarItems.forEach(function(item, idx){
      const btn = pillarButtons[idx];
      if(!btn) return;
      setText(btn.querySelector('.pillar-name'), item.name);
      setText(btn.querySelector('.pillar-note'), item.note);
      btn.setAttribute('aria-label', item.note || '');
    });

    setText(document.querySelector('.showcase .section-title'), data.showcase && data.showcase.title);
    const slider = document.querySelector('.slider');
    if(slider) slider.setAttribute('aria-label', data.showcase && data.showcase.region || '');
    const leftArrow = document.querySelector('.arrow.left');
    if(leftArrow) leftArrow.setAttribute('aria-label', data.showcase && data.showcase.prev || '');
    const rightArrow = document.querySelector('.arrow.right');
    if(rightArrow) rightArrow.setAttribute('aria-label', data.showcase && data.showcase.next || '');

    document.querySelectorAll('.logo-card[data-slug]').forEach(function(card){
      const slug = card.dataset.slug;
      const caption = data.captions && data.captions[slug];
      if(caption){
        card.dataset.caption = caption;
        card.setAttribute('aria-label', caption);
      }
      setBadgeText(card, '.badge-archived', data.badges && data.badges.archived);
      setBadgeText(card, '.badge-active', data.badges && data.badges.active);
    });

    const inaiSpotlight = document.querySelector('.inai');
    if(inaiSpotlight){
      if(data.inaiSpotlight && data.inaiSpotlight.aria){
        inaiSpotlight.setAttribute('aria-label', data.inaiSpotlight.aria);
      }
      const badge = inaiSpotlight.querySelector('.badge-outcome');
      setText(badge, data.badges && data.badges.outcome);
    }

    const portraitImg = document.querySelector('.portrait-inner img');
    if(portraitImg) portraitImg.alt = data.aria && data.aria.portrait_alt || '';
    const figcaption = document.querySelector('.portrait figcaption');
    setText(figcaption, data.aria && data.aria.portrait_caption);
    const modalClose = document.querySelector('.modal-close');
    if(modalClose) modalClose.setAttribute('aria-label', data.aria && data.aria.modal_close || '');
    const langSwitcher = document.querySelector('.lang-switcher');
    if(langSwitcher) langSwitcher.setAttribute('aria-label', data.aria && data.aria.lang_switcher || '');

    const tooltip = document.querySelector('.tooltip');
    if(tooltip){
      tooltip.classList.remove('show', 'above', 'below');
      tooltip.textContent = '';
    }
  }

  function fillActiveModal(){
    const body = document.getElementById('case-body');
    if(!body) return;
    const slug = body.dataset.slug;
    if(!slug) return;
    const wrapper = body.closest('.case');
    if(!wrapper) return;
    const data = translations[currentLang] || translations[defaultLang];
    if(!data) return;
    if(modalFillers[slug]){
      modalFillers[slug](wrapper, data.modals && data.modals[slug]);
    }else if(data.cases && data.cases[slug]){
      fillCase(wrapper, data.cases[slug]);
    }
  }

  function updateLangButtons(){
    langBtns.forEach(function(btn){
      const isActive = btn.dataset.lang === currentLang;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });
  }

  function applyTranslations(){
    updateTemplates(currentLang);
    applyBaseTranslations();
    fillActiveModal();
    updateLangButtons();
    document.documentElement.lang = currentLang;
    safeSet(storageKey, currentLang);
  }

  function switchLanguage(lang){
    if(!lang || !translations[lang] || lang === currentLang) return;
    currentLang = lang;
    applyTranslations();
  }

  langBtns.forEach(function(btn){
    btn.addEventListener('click', function(){
      switchLanguage(btn.dataset.lang);
    });
  });

  document.addEventListener('romanempire:modal-populated', function(){
    fillActiveModal();
  });

  applyTranslations();

  window.RomanEmpireI18n = {
    get current(){ return currentLang; },
    data: translations,
    switch: switchLanguage,
    refreshModal: fillActiveModal,
    apply: applyTranslations
  };
})();
"""

js_code = JS_TEMPLATE % {"translations": json.dumps(translations, ensure_ascii=False, indent=2)}
Path("assets/js/i18n.js").write_text(js_code, encoding="utf-8")
