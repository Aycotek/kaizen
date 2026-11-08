# Kaizen

**Arrêtez d'automatiser le gaspillage.**

*Il fait le tour de l'atelier avant de toucher au clavier.*

[English](../README.md)

---

Vous le connaissez. Trente ans d'usine. Avant qu'on achète une machine, il passe une matinée à
regarder les gens travailler, puis revient avec une feuille : trois étapes à supprimer, un
formulaire à changer, et une machine beaucoup plus petite.

Votre agent IA fait l'inverse. Demandez-lui « d'ajouter de l'IA au tri de notre support », et il
commence à écrire un classifieur. Personne n'a regardé pourquoi le tri prend du temps.

**Kaizen met cet homme dans votre agent.** Avant d'automatiser quoi que ce soit, il va voir le
travail réel, le cartographie, trouve les gaspillages, corrige la cause racine, et n'automatise
qu'ensuite ce qui reste, avec un point de départ mesuré.

## L'échelle

Chaque étape d'un processus monte cette échelle et s'arrête au premier barreau qui fonctionne :

1. **Supprimer** : cette étape doit-elle exister ?
2. **Combiner ou réordonner** : moins de passages de relais, contrôles au début.
3. **Simplifier** : moins de champs, des valeurs par défaut, une seule source de vérité.
4. **Rendre l'erreur impossible** (poka-yoke) : liste déroulante, champ obligatoire, contrôle à la saisie.
5. **Automatiser par des règles** : fonction de l'outil existant, formule, script.
6. **Automatiser par l'IA** : seulement pour lire ou juger du contenu non structuré en volume.
7. **Garder l'humain** : jugement, relation, responsabilité.

L'IA est au barreau 6. L'essentiel du gain est souvent aux barreaux 1 à 4, sans une ligne de code.

## Les skills

| Commande | Ce qu'elle fait |
|----------|-----------------|
| `/kaizen [lite\|full\|ultra]` | Le mode : aller voir, cartographier, supprimer les gaspillages, corriger la cause racine, monter l'échelle, mesurer, lancer la plus petite expérience. Produit une fiche kaizen d'un écran. |
| `/kaizen-map` | SIPOC, tableau de l'existant avec délais et rendement du flux, couloirs Mermaid, et un **vrai fichier BPMN 2.0** qui s'ouvre dans bpmn.io, Camunda Modeler ou Signavio. |
| `/kaizen-waste` | Chasse aux gaspillages du travail de bureau (DOWNTIME), classés par heures perdues par semaine, chaque ligne justifiée par une preuve. |
| `/kaizen-why` | Analyse de cause racine : 5 pourquoi avec preuves, Ishikawa, actions de confinement, de correction et de prévention (esprit 8D). Marche aussi pour les bugs. |
| `/kaizen-roi` | Le business case honnête : coût des erreurs du nouveau système, seuil de rentabilité, option moins chère, critères d'arrêt fixés à l'avance. |
| `/kaizen-sop` | Faire durer : procédure d'une page, check-list au poste, détrompeurs, plan de surveillance. |
| `/kaizen-help` | Aide-mémoire. |

Les skills se déclenchent aussi tout seuls quand vous décrivez la tâche : « peut-on automatiser la
validation de nos factures ? », « cartographie ce processus d'intégration », « pourquoi ça se
reproduit ? ».

## Installation

**Claude Code**, en plugin :

```text
/plugin marketplace add Aycotek/kaizen
/plugin install kaizen@kaizen
```

**Claude Code**, à la main : copiez les dossiers de `skills/` dans `~/.claude/skills/` (tous les
projets) ou `.claude/skills/` (un seul projet).

**Agents qui lisent `AGENTS.md`** (Codex, Cursor et d'autres) : copiez [AGENTS.md](../AGENTS.md) à
la racine de votre projet.

Les skills sont rédigés en anglais, mais répondent dans la langue de l'utilisateur.

## Ce que Kaizen ne fera pas

- Inventer des chiffres : un chiffre inconnu est marqué inconnu, avec la façon de le mesurer.
- Accuser quelqu'un : un défaut vient toujours de la façon dont le travail est organisé.
- Supprimer un contrôle sans demander pourquoi il existe.
- Pousser l'IA là où un formulaire, une règle ou un modèle de réponse suffit.

## Auteur

[Arthur Rolland](https://www.linkedin.com/in/arthur-rolland1/) : chef de projet SI et processus,
Lean Six Sigma Green Belt, BPMN, IA appliquée aux métiers. Kaizen met en boîte la méthode que
j'applique sur le terrain avec les équipes opérationnelles.

Licence MIT.
