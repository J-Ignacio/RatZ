<div align="center">
  <!-- 🖼️ PLACE BANNER IMAGE HERE (e.g., <img src="docs/assets/banner.png" alt="Ratz Banner">) -->

  # 🐀 RATZ 🧟

  **"In the sewers, the dead don't stay dead. And the rats? They're the least of your problems."**

  [![License](https://img.shields.io/badge/License-MIT-darkred.svg)](LICENSE)
  [![Status](https://img.shields.io/badge/Status-In_Development-black.svg)]()
</div>

---

## 🩸 The Premise

> *Day 43. The surface is completely gone. We thought the sewers would be safe, that the steel and concrete would keep the biters out. We were wrong. The infection seeped down through the grates. Now, it’s just us, the dark, and the echoes of dragging feet. You scavenge what you can, build what you must, and try to make it to tomorrow. Once you die down here, you join the horde. No second chances.*

Welcome to **Ratz**, a gritty, unforgiving 2D zombie survival experience where every bullet is precious and the darkness is your greatest enemy.

---

## 🔫 Key Features

- **Brutal Scavenging:** Search abandoned maintenance shafts for scraps, medicine, and ammo. Resources are scarce, and noise attracts the horde.
- **Makeshift Crafting:** Tape a flashlight to a pipe. Combine rags and alcohol. Your survival depends on what you can build from the ruins.
- **Permadeath:** When you die, that's it. Your next survivor will have to navigate the same sewers, and they might just find your previous character... wandering.
- **Dynamic Lighting:** A 2D line-of-sight system means you only see what your flashlight reveals. The shadows hide horrors.
- **The Horde System:** Zombies are attracted to sound and light. Fire a gun, and you better be ready to run.

<div align="center">
  <!-- 🖼️ PLACE GAMEPLAY GIF HERE (e.g., <img src="docs/assets/gameplay.gif" alt="Ratz Gameplay">) -->
</div>

---

## ⚙️ Tech Stack

Built from the ground up for performance and atmosphere, leaving the chaos for the gameplay, not the codebase.

- **Game Engine:** [Godot 4.x] / [Unity] / [Custom] *(Update as needed)*
- **Language:** C# / GDScript / C++
- **Graphics:** Aseprite (Pixel Art), Custom 2D Lighting Shaders
- **Audio:** FMOD for dynamic, spatial soundscapes

---

## 🔧 Installation

To compile the survivor's toolkit and run the game source locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ratz.git
   cd ratz
   ```

2. **Setup the Environment**
   - Ensure you have [Godot Engine 4.x / required engine] installed.
   - Open the engine and import the `project.godot` (or equivalent project file).

3. **Install Dependencies**
   - *(If using external plugins or submodules)*
   ```bash
   git submodule update --init --recursive
   ```

4. **Build and Run**
   - Hit the `Play` button in the editor, or build via command line:
   ```bash
   # Example build command
   ./build_scripts/build_linux.sh
   ```

---

## 🎮 Controls

Survival relies on reflexes. Know your gear.

| Action | Keybinding |
| :--- | :--- |
| **Move** | `W` `A` `S` `D` |
| **Aim** | `Mouse Cursor` |
| **Fire/Melee** | `Left Click` |
| **Interact / Scavenge** | `E` |
| **Toggle Flashlight** | `F` |
| **Inventory / Crafting** | `Tab` |
| **Sprint** | `Shift` (Consumes Stamina) |

---

## 🗺️ Roadmap

The infection spreads, but so does our development.

### ✅ Surviving (Done)
- [x] Core 2D movement and collision
- [x] Basic zombie AI and pathfinding
- [x] Inventory and fundamental crafting logic
- [x] Dynamic line-of-sight lighting

### 🦠 Infected (Pending)
- [ ] Procedural sewer generation
- [ ] Advanced noise-propagation system for AI
- [ ] Implement "Previous Player Zombie" feature (Permadeath persistence)
- [ ] Sound design overhaul (FMOD integration)
- [ ] Boss mutation encounters

---

## 📜 License & Credits

**License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. *(You can survive, but don't steal.)*

**Credits**
- **Lead Developer / Designer:** [Your Name/Handle]
- **Pixel Art:** [Artist Name]
- **Audio:** [Audio Engineer]
- *Special thanks to the open-source community for the survival tools.*

<div align="center">
  <br>
  <i>"Keep your flashlight charged and your shotgun loaded."</i>
</div>