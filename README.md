# Nebula CTF - Level 14

Complete walkthrough and exploit solution for Level 14 of the "Nebula" CTF, achieved via black-box reverse engineering of a position-dependent encryption algorithm.

## Introduction

**Nebula** is an offensive security and vulnerability analysis CTF (Capture The Flag) platform developed by **Exploit Education**.  
Hosted on a Linux-based virtual machine, it provides progressive challenges covering:

- Privilege escalation
- Reverse engineering
- Binary exploitation
- C programming and exploit scripting

**Level 14** presents a cipher deconstruction and reverse engineering challenge.

## Challenge Description

In Level 14, the target executable accepts an input string and returns an encrypted output string.

The cipher algorithm manipulates each character of the input by applying mathematical transformations conditioned on the **index position** of the character itself.

## Approach and Methodology

### Phase 1: Static Analysis

Enumeration of accessible files, associated filesystem permissions, and environmental clues within the `/home/flag14` directory to scope the challenge constraints.

### Phase 2: Algorithm Reconstruction

Reconstructed the cipher logic using **black-box analysis** by systematically mapping test input patterns against their corresponding encrypted outputs to determine character shift offsets.

### Phase 3: Cipher Reversal and Validation

Once the positional transformation was determined, developed a decryption algorithm to reverse the cipher. Applied this script to decrypt the contents of `token.txt`, successfully uncovering the cleartext password.

### Phase 4: Exploitation and Flag Capture

Authenticated as the target user `flag14` using the recovered password, then executed `/bin/getflag` to obtain the confirmation: `"You have successfully executed getflag on a target account"`, thereby completing the challenge.

## Additional Details

For a complete breakdown including the attack tree analysis and step-by-step methodologies, refer to the presentation `Nebula14_presentazione.pdf`.

## Repository Structure

- `Soluzioni/decrypter.c` - C implementation of the decryption exploit.
- `Soluzioni/decrypter.py` - Python implementation of the decryption exploit.
- `Nebula14_presentazione.pdf` - Educational presentation delivered during the university lecture.

## Team

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/TherealBarnar">
        <img src="https://github.com/TherealBarnar.png" width="80px;" alt="Giuseppe D'Avino"/><br />
        <sub><b>Giuseppe D'Avino</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/carmineh">
        <img src="https://github.com/carmineh.png" width="80px;" alt="Carmine Calabrese"/><br />
        <sub><b>Carmine Calabrese</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/marcociano">
        <img src="https://github.com/marcociano.png" width="80px;" alt="Marco Ciano"/><br />
        <sub><b>Marco Ciano</b></sub>
      </a>
    </td>
  </tr>
</table>

---
