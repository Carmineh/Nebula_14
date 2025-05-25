# Nebula CTF - Livello 14 🔐

Soluzione completa del livello 14 della CTF "Nebula", realizzata tramite reverse engineering di un algoritmo di cifratura posizionale.

## 🖥️ Introduzione

**Nebula** è una delle CTF (Capture The Flag) create da **Exploit Education** per migliorare le proprie competenze in sicurezza informatica e analisi di vulnerabilità.  
La CTF si svolge su una macchina virtuale Linux-based, progettata per offrire sfide progressive in ambito di:

- Privilege escalation
- Reverse engineering
- Exploiting
- Programmazione in C e scripting

Il **livello 14** presenta una sfida di decifrazione/reversing.

## 📜 Descrizione del Problema

Nel livello 14, l’eseguibile fornito accetta una stringa in input e restituisce un output cifrato.

L'algoritmo manipola i caratteri della stringa in ingresso applicando trasformazioni condizionate dalla **posizione** dei caratteri stessi.

## 🧠 Soluzione e Approccio

### 🔍 Fase 1: Analisi statica

Studio dei file a nostra disposizione, eventuali permessi ad essi associati che permetta di trovare "indizi" per risolvere la sfida CTF.

### 🔁 Fase 2: Ricostruzione dell’algoritmo

Per ricostruire l'algoritmo è stata usata una tecnica di reverse engineering chiamata **black-box analysis**, ovvero studiare la correlazione tra input e output dati al programma.

### 🧪 Fase 3: Validazione

Una volta risaliti all'algoritmo è stato semplice ricostruire sia l'algoritmo stesso, che un algoritmo che permettesse di decifrare le stringhe, ergo decifrare la stringa contenuta in _token.txt_ che è risultata essere poi la password

### 🚩Fase 4: Cattura della Bandiera

Tramite il token decifrato (che si è scoperto poi essere la password) abbiamo effettuato l'accesso all'account _flag14_ ed eseguito il comando _/bin/getflag_ che ha permesso di ricevere l'output desiderato "**You have successfully executed getflag on a target account**" e quindi vinto la sfida.

## ℹ️ Informazioni

Per informazioni più dettagliate è consigliato visionare la presentazione _Nebula14_presentazione.pdf_ per un albero di attacco completo e una spiegazione dei passi più dettagliata.

## 📁 Contenuto della Repository

- `/soluzioni/decrypt.c` → Script utilizzato per decifrare la stringa (C).
- `/soluzioni/decrypt.py` → Script utilizzato per decifrare la stringa (python).
- `Nebula14_presentazione.pdf` → Presentazione didattica svolta in aula a tutti gli studenti del corso

## 👨‍👩‍👧 Team

<table align="center">
  <tr>
      <td align="center">
      <a href="https://github.com/TherealBarnar">
        <img src="https://github.com/TherealBarnar.png" width="80px;" alt=""/><br />
        <sub><b>Giuseppe D'Avino</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/carmineh">
        <img src="https://github.com/carmineh.png" width="80px;" alt=""/><br />
        <sub><b>Carmine Calabrese</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/marcociano">
        <img src="https://github.com/marcociano.png" width="80px;" alt=""/><br />
        <sub><b>Marco Ciano</b></sub>
      </a>
    </td>
  </tr>
</table>

---
