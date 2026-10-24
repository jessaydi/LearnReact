# React pour devs backend

Un cours en français sur les fondamentaux de React 19, écrit pour un développeur backend Python et C#. Chaque notion est expliquée pas à pas, avec des analogies, du code commenté, des démos interactives, des exercices corrigés et des quiz.

## Lire le cours

Ouvre `index.html` dans ton navigateur. La page fonctionne hors ligne. Seules les polices et la coloration du code viennent d'Internet ; sans connexion, la page s'affiche avec les polices système et du code non coloré.

Ta progression (modules marqués comme lus) est enregistrée dans le navigateur, pas dans le dépôt.

## Les modules

| N° | Module | Contenu |
|----|--------|---------|
| 00 | Penser déclaratif | TaskFlow, le DOM, le cycle données → React → DOM → écran |
| 01 | Les bases de JavaScript | types, objets, tableaux, fonctions, références, async, table Python / C# |
| 02 | Anatomie d'un projet | Node, npm, Vite, chaque fichier d'un projet, organisation d'un vrai projet |
| 03 | Composants et JSX | ce que devient le JSX, les 10 règles, découper un écran |
| 04 | Props | props, `children`, flux à sens unique, callbacks |
| 05 | useState | état, rendu, objets et tableaux sans mutation |
| 06 | Événements, listes, formulaires | conditions, `key`, champs contrôlés |
| 07 | Le cycle de rendu | ce qui déclenche un rendu, pureté, remonter l'état |
| 08 | useEffect | dépendances, nettoyage, chargement de données, pièges |
| 09 | Règles et autres hooks | `useRef`, `useMemo`, `useCallback`, `useReducer`, React Compiler |
| 10 | Context et useContext | Provider + custom hook, coût d'un contexte |
| 11 | Custom hooks | extraire et réutiliser de la logique |
| 12 | Suspense et lazy | chargement déclaratif, découpage du code, `use` |
| 13 | Error boundaries | capturer les erreurs, `react-error-boundary` |
| 14 | Débugger | DevTools, méthode, dictionnaire des erreurs |
| 15 | Lire un projet, ajouter une feature | ordre de lecture, où placer l'état |
| 16 | Travailler avec l'IA | prompts, signaux d'alerte en relecture |
| 17 | Antisèche et suite | résumé des hooks, glossaire, projet fil rouge |

Tous les modules ont été retravaillés pour avancer pas à pas, avec des schémas, une quarantaine de démos interactives, des aides à la décision, des exercices corrigés et un encadré « En bref » par module.

## Organisation du dépôt

```
index.html        la page complète, générée : c'est elle qu'on ouvre
src/              les sources, un fichier par module ou groupe de modules
  00_styles.html                              titre, polices et feuille de style
  10_m00-m01_declaratif-javascript.html
  20_m02-m05_projet-jsx-props-usestate.html
  30_m06_evenements-listes-formulaires.html
  31_m07_cycle-de-rendu.html
  32_m08_useeffect.html
  40_m09_regles-autres-hooks.html
  41_m10_context.html
  42_m11_custom-hooks.html
  50_m12_suspense-lazy.html
  51_m13_error-boundaries.html
  52_m14_debugger.html
  60_m15_lire-un-projet.html
  61_m16_ia.html
  62_m17_antiseche.html
  90_script_page.html                         quiz, progression, sommaire, copier le code
  91_script_demos.html                        les démos des modules 00 à 06
  92_script_demos_m07-m17.html                les démos des modules 07 à 17
tools/build.py    assemble src/ en index.html
```

## Modifier le cours

1. Modifie le fichier concerné dans `src/`. Dans les balises `<code>`, écris le code tel quel (`<div>`, `a < b`) : le script l'échappe.
2. Régénère la page (Python 3.9 ou plus, aucune dépendance) :

   ```bash
   python3 tools/build.py index.html --standalone
   ```

3. Ouvre `index.html` pour vérifier, puis commite les sources et la page.

Le sommaire et le pied de chaque module (« Marquer comme lu », « Module suivant ») sont générés à partir des balises `<section class="module" id="mXX" data-short="...">`. Chaque module doit se terminer par `</section><!--/mXX-->`.

## Sources

Le contenu suit la documentation officielle de React (version 19.3 du 9 septembre 2026) :

- [React Versions](https://react.dev/versions)
- [React 19.3](https://react.dev/blog/2026/09/09/react-19-3)
- [React Compiler v1.0](https://react.dev/blog/2025/10/07/react-compiler-1)
- [Sunsetting Create React App](https://react.dev/blog/2025/02/14/sunsetting-create-react-app)
- [Component (error boundaries)](https://react.dev/reference/react/Component)
- [Keeping Components Pure](https://react.dev/learn/keeping-components-pure)
- [Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state)
- [You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect)
- [Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)
