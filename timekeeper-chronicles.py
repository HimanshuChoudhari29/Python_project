import time
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03):
    """Print text with typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_banner(title):
    """Print a beautiful banner for each scene."""
    width = 60
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width)

def print_scene_banner(scene_name):
    """Print scene-specific banner."""
    banner = f"""
    ╔══════════════════════════════════════════════════════╗
    ║                    {scene_name:^36}                  ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(banner)

class TimekeeperChronicles:
    def __init__(self):
        self.player_name = ""
        self.inventory = []
        self.health = 100
        self.knowledge = 0
        self.courage = 0  # FIXED: Starts at 0
        self.compassion = 0
        self.current_chapter = 1
        self.game_state = "playing"
        
        # Progress flags
        self.has_crystal_chronicle = False
        self.saved_owl = False
        self.has_time_sap = False
        self.has_temporal_hammer = False
        self.has_lumina_blossom = False
        
        # Chapter 2 flags
        self.mechanical_fixed = False
        self.organic_fixed = False
        self.elemental_fixed = False
        self.helped_robot = False
        
        # Track visited areas for courage bonuses
        self.visited_volcanic = False
        self.visited_mechanical = False
        self.visited_garden = False
        
        # Ending achieved
        self.ending = ""
    
    def show_stats(self):
        """Display player stats."""
        print(f"\n{'═'*60}")
        print(f"❤️  HEALTH: {self.health}/100 | 🧠 KNOWLEDGE: {self.knowledge} | 🛡️  COURAGE: {self.courage} | ❤️  COMPASSION: {self.compassion}")
        if self.inventory:
            print(f"🎒 INVENTORY: {', '.join(self.inventory)}")
        print(f"{'═'*60}")
    
    def get_choice(self, options):
        """Get valid choice from player."""
        while True:
            try:
                choice = input("\nYour choice: ").strip()
                if choice in options:
                    return choice
                else:
                    type_text(f"Please enter one of: {', '.join(options)}")
            except:
                type_text("Invalid input. Please try again.")
    
    # ==================== MAIN GAME FLOW ====================
    
    def start_game(self):
        """Start the game."""
        clear_screen()
        print_banner("TIMEKEEPER CHRONICLES")
        print("\n" + "~" * 60)
        print("      AN EPIC TEXT ADVENTURE WITH MULTIPLE ENDINGS")
        print("~" * 60)
        
        type_text("\nWhat is your name, destined Timekeeper? ")
        self.player_name = input("> ").strip()
        if not self.player_name:
            self.player_name = "Hero"
        
        type_text(f"\nWelcome, {self.player_name}! Your journey begins...")
        time.sleep(2)
        self.chapter_1()
    
    def chapter_1(self):
        """Chapter 1: The Awakening."""
        clear_screen()
        print_banner("CHAPTER 1: THE AWAKENING")
        time.sleep(1)
        
        type_text(f"\n{self.player_name}, you awaken in a strange circular chamber.")
        type_text("Ancient machinery hums around you. Dust floats in beams of light.")
        type_text("A voice echoes: 'You are the last Timekeeper. The Chrono-Core fails.'")
        type_text("'Restore balance. Begin your journey...'")
        
        input("\nPress Enter to begin...")
        self.scene_1_entrance()
    
    def scene_1_entrance(self):
        """Scene 1: Entrance Chamber."""
        while self.game_state == "playing" and self.current_chapter == 1:
            clear_screen()
            print_scene_banner("THE AWAKENING CHAMBER")
            
            type_text("\nYou stand in a circular chamber with three glowing archways:")
            type_text("1. 🔵 BLUE ARCHWAY - Mechanical humming sounds")
            type_text("2. 🟢 GREEN ARCHWAY - Smells of earth and growth")
            type_text("3. 🔴 RED ARCHWAY - Flickers with unstable energy")
            type_text("\nIn the center, a CRYSTAL CHRONICLE glows on a pedestal.")
            
            self.show_stats()
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Take the Crystal Chronicle")
            print("2. Enter BLUE archway (Mechanical)")
            print("3. Enter GREEN archway (Garden)")
            print("4. Enter RED archway (Volcanic)")
            print("5. Ready to proceed to Chapter 2")
            
            choice = self.get_choice(["1", "2", "3", "4", "5"])
            
            if choice == "1":
                if not self.has_crystal_chronicle:
                    type_text("\nYou take the CRYSTAL CHRONICLE.")
                    type_text("It glows warmly, showing glimpses of past and future.")
                    self.inventory.append("Crystal Chronicle")
                    self.has_crystal_chronicle = True
                    self.knowledge += 15
                else:
                    type_text("\nYou already have the Chronicle.")
                input("\nPress Enter to continue...")
            
            elif choice == "2":
                self.scene_1_mechanical()
            
            elif choice == "3":
                self.scene_1_garden()
            
            elif choice == "4":
                self.scene_1_volcanic()
            
            elif choice == "5":
                if self.has_crystal_chronicle:
                    self.complete_chapter_1()
                else:
                    type_text("\nYou should take the Crystal Chronicle first!")
                    input("\nPress Enter to continue...")
    
    def scene_1_mechanical(self):
        """Mechanical Labyrinth scene."""
        clear_screen()
        print_scene_banner("MECHANICAL LABYRINTH")
        
        # FIXED: Add courage for entering dangerous area (first time only)
        if not self.visited_mechanical:
            type_text("\nYou bravely enter the dangerous mechanical area!")
            type_text("+10 Courage for facing danger!")
            self.courage += 10
            self.visited_mechanical = True
        else:
            type_text("\nYou return to the mechanical labyrinth.")
        
        type_text("\nA mechanical owl is trapped under a fallen gear!")
        
        while True:
            self.show_stats()
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Try to free the owl")
            print("2. Search for tools")
            print("3. Examine control panel")
            print("4. Return to entrance")
            
            choice = self.get_choice(["1", "2", "3", "4"])
            
            if choice == "1":
                if not self.saved_owl:
                    type_text("\nYou try to lift the heavy gear...")
                    if self.courage >= 20 or "Temporal Hammer" in self.inventory:
                        type_text("\nSuccess! The owl is freed!")
                        type_text("It gives you a GEAR KEY in gratitude.")
                        self.inventory.append("Gear Key")
                        self.saved_owl = True
                        self.compassion += 20
                        self.courage += 10  # Bonus for success
                        type_text("+10 Courage bonus!")
                    else:
                        type_text("\nThe gear is too heavy. You need more courage.")
                        type_text("Current courage: " + str(self.courage) + "/20 required")
                        type_text("+5 Courage for trying!")
                        self.courage += 5  # Always get some courage for trying
                        self.health -= 5
                else:
                    type_text("\nThe owl is already free and happily hooting.")
                input("\nPress Enter to continue...")
            
            elif choice == "2":
                if "Oil Can" not in self.inventory:
                    type_text("\nYou find an OIL CAN in a toolbox.")
                    self.inventory.append("Oil Can")
                    type_text("+5 Courage for finding useful tools!")
                    self.courage += 5
                else:
                    type_text("\nYou've already searched here.")
                input("\nPress Enter to continue...")
            
            elif choice == "3":
                if self.has_crystal_chronicle:
                    type_text("\nThe Chronicle activates the panel!")
                    type_text("You learn about time mechanics. +10 Knowledge")
                    self.knowledge += 10
                else:
                    type_text("\nThe panel shows complex symbols you don't understand.")
                input("\nPress Enter to continue...")
            
            elif choice == "4":
                return
    
    def scene_1_garden(self):
        """Eternal Garden scene."""
        clear_screen()
        print_scene_banner("ETERNAL GARDEN")
        
        # FIXED: Add courage for exploring new area
        if not self.visited_garden:
            type_text("\nYou explore the mysterious garden.")
            type_text("+5 Courage for venturing into the unknown!")
            self.courage += 5
            self.visited_garden = True
        else:
            type_text("\nYou return to the peaceful garden.")
        
        type_text("\nA beautiful garden frozen in time.")
        type_text("A crystal tree with a dying branch stands at the center.")
        
        while True:
            self.show_stats()
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Examine the crystal tree")
            print("2. Collect glowing flowers")
            print("3. Look for the garden keeper")
            print("4. Return to entrance")
            
            choice = self.get_choice(["1", "2", "3", "4"])
            
            if choice == "1":
                type_text("\nThe tree's sap is liquid time.")
                if "Oil Can" in self.inventory:
                    type_text("\nYou use oil to heal the branch. It produces TIME SAP.")
                    self.inventory.append("Time Sap")
                    self.has_time_sap = True
                    self.compassion += 15
                    type_text("+5 Courage for healing nature!")
                    self.courage += 5
                else:
                    type_text("\nThe branch needs healing, but you lack tools.")
                input("\nPress Enter to continue...")
            
            elif choice == "2":
                if "Lumina Blossom" not in self.inventory:
                    type_text("\nYou collect a LUMINA BLOSSOM.")
                    self.inventory.append("Lumina Blossom")
                    self.has_lumina_blossom = True
                    type_text("+3 Courage for finding magical items!")
                    self.courage += 3
                else:
                    type_text("\nYou already have the blossom.")
                input("\nPress Enter to continue...")
            
            elif choice == "3":
                type_text("\nA gentle voice whispers: 'Heal the tree with care...'")
                type_text("The garden appreciates your presence. +5 Compassion")
                self.compassion += 5
                input("\nPress Enter to continue...")
            
            elif choice == "4":
                return
    
    def scene_1_volcanic(self):
        """Volcanic Forge scene."""
        clear_screen()
        print_scene_banner("VOLCANIC FORGE")
        
        # FIXED: MAJOR BUG FIX - Courage added immediately upon entering
        if not self.visited_volcanic:
            type_text("\n🔥 You bravely enter the intensely hot volcanic forge!")
            type_text("🛡️  +15 COURAGE for facing extreme danger!")
            self.courage += 15  # FIXED: Now courage increases immediately
            self.visited_volcanic = True
        else:
            type_text("\nYou return to the scorching volcanic forge.")
        
        type_text("\nIntense heat hits you! A forge holds an unfinished hammer.")
        type_text("The heat is dangerous! (-15 health)")
        self.health -= 15
        
        while True:
            self.show_stats()
            if self.health <= 0:
                type_text("\n❌ You succumb to the heat...")
                self.game_over("Heat Exhaustion")
                return
                
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Try to complete the hammer (requires 30 courage)")
            print("2. Search for protective gear")
            print("3. Study the forge's patterns")
            print("4. Retreat to entrance")
            
            choice = self.get_choice(["1", "2", "3", "4"])
            
            if choice == "1":
                type_text("\nYou approach the blazing forge...")
                type_text(f"Your courage: {self.courage}/30 needed")
                if self.courage >= 30:
                    type_text("\n✅ Your courage lets you withstand the heat!")
                    type_text("You complete the TEMPORAL HAMMER!")
                    self.inventory.append("Temporal Hammer")
                    self.has_temporal_hammer = True
                    self.courage += 25  # Big bonus for success
                    type_text("+25 Courage for incredible bravery!")
                else:
                    type_text("\n🔥 The heat is too intense! But you learn from the attempt.")
                    type_text("+10 Courage for facing your fears!")
                    self.courage += 10  # Good courage gain even if fail
                    self.health -= 10   # Reduced penalty
                input("\nPress Enter to continue...")
            
            elif choice == "2":
                if "Heat Gloves" not in self.inventory:
                    type_text("\nYou find HEAT-RESISTANT GLOVES.")
                    self.inventory.append("Heat Gloves")
                    type_text("+8 Courage for finding protective gear!")
                    self.courage += 8
                    type_text("These will help with hot objects.")
                else:
                    type_text("\nYou already have the heat gloves.")
                input("\nPress Enter to continue...")
            
            elif choice == "3":
                type_text("\nYou study the forge's ancient runes.")
                type_text("+15 Knowledge about elemental time.")
                self.knowledge += 15
                type_text("+5 Courage for learning in dangerous conditions!")
                self.courage += 5
                input("\nPress Enter to continue...")
            
            elif choice == "4":
                return
    
    def complete_chapter_1(self):
        """Complete Chapter 1."""
        clear_screen()
        print_banner("CHAPTER 1 COMPLETE!")
        
        type_text(f"\n{self.player_name}, you have gathered what you need.")
        type_text("A portal opens before you, leading to the Chrono-Core...")
        
        # Chapter completion bonus - FIXED: Now gives courage
        self.health = min(100, self.health + 20)
        self.courage += 20  # FIXED: Big courage bonus for completing chapter
        self.knowledge += 10
        self.compassion += 10
        
        type_text("\n🎁 CHAPTER COMPLETION BONUS:")
        type_text("+20 Health, +20 Courage, +10 Knowledge, +10 Compassion")
        
        input("\nPress Enter to continue to Chapter 2...")
        self.current_chapter = 2
        self.chapter_2()
    
    # ==================== CHAPTER 2 ====================
    
    def chapter_2(self):
        """Chapter 2: Heart of Time."""
        clear_screen()
        print_banner("CHAPTER 2: HEART OF TIME")
        time.sleep(1)
        
        type_text("\nYou arrive at the CHRONO-CORE chamber.")
        type_text("A massive crystal sphere floats in the center, with three fractures.")
        type_text("Each fracture threatens to unravel time itself!")
        
        # FIXED: Courage for reaching Chapter 2
        type_text("\n🛡️  +10 Courage for reaching the Chrono-Core!")
        self.courage += 10
        
        input("\nPress Enter to continue...")
        self.scene_2_core_chamber()
    
    def scene_2_core_chamber(self):
        """Core Chamber scene."""
        while self.game_state == "playing" and self.current_chapter == 2:
            clear_screen()
            print_scene_banner("CHRONO-CORE CHAMBER")
            
            fixed_count = sum([self.mechanical_fixed, self.organic_fixed, self.elemental_fixed])
            stability = 40 + (fixed_count * 20)
            
            type_text(f"\nCore Stability: {stability}%")
            type_text("\nThree fractures need healing:")
            status = []
            if self.mechanical_fixed: status.append("🔵 Mechanical: HEALED")
            else: status.append("🔵 Mechanical: BROKEN")
            if self.organic_fixed: status.append("🟢 Organic: HEALED")
            else: status.append("🟢 Organic: BROKEN")
            if self.elemental_fixed: status.append("🔴 Elemental: HEALED")
            else: status.append("🔴 Elemental: BROKEN")
            
            for s in status:
                type_text(s)
            
            self.show_stats()
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Heal MECHANICAL fracture (Blue)")
            print("2. Heal ORGANIC fracture (Green)")
            print("3. Heal ELEMENTAL fracture (Red)")
            print("4. Check damaged robot assistant")
            
            if fixed_count == 3:
                print("5. ACTIVATE CORE RESTORATION")
            
            options = ["1", "2", "3", "4"]
            if fixed_count == 3:
                options.append("5")
            
            choice = self.get_choice(options)
            
            if choice == "1":
                self.heal_mechanical_fracture()
            
            elif choice == "2":
                self.heal_organic_fracture()
            
            elif choice == "3":
                self.heal_elemental_fracture()
            
            elif choice == "4":
                self.check_robot()
            
            elif choice == "5" and fixed_count == 3:
                self.complete_chapter_2()
    
    def heal_mechanical_fracture(self):
        """Heal the mechanical fracture."""
        clear_screen()
        print_scene_banner("MECHANICAL FRACTURE")
        
        if self.mechanical_fixed:
            type_text("\nThis fracture is already healed.")
            input("\nPress Enter to continue...")
            return
        
        type_text("\nGears grind painfully. A mainspring is overwound.")
        
        print("\n" + "─" * 50)
        print("How will you heal it?")
        print("1. Use Temporal Hammer (if you have it)")
        print("2. Use Gear Key (if you have it)")
        print("3. Try manual repair (dangerous - requires courage)")
        print("4. Return to core chamber")
        
        choice = self.get_choice(["1", "2", "3", "4"])
        
        if choice == "1":
            if "Temporal Hammer" in self.inventory:
                type_text("\nYou use the hammer to safely release tension!")
                type_text("✅ MECHANICAL FRACTURE HEALED!")
                self.mechanical_fixed = True
                self.courage += 15
                type_text("+15 Courage for precise repair!")
            else:
                type_text("\nYou don't have the Temporal Hammer.")
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            if "Gear Key" in self.inventory:
                type_text("\nThe Gear Key perfectly aligns the mechanisms!")
                type_text("✅ MECHANICAL FRACTURE HEALED!")
                self.mechanical_fixed = True
                self.knowledge += 10
                self.courage += 10
                type_text("+10 Courage for clever solution!")
            else:
                type_text("\nYou don't have the Gear Key.")
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            type_text("\nYou attempt manual repair...")
            type_text(f"Your courage: {self.courage}/40 needed")
            if self.courage >= 40:
                type_text("\n✅ Success through sheer bravery!")
                type_text("✅ MECHANICAL FRACTURE HEALED!")
                self.mechanical_fixed = True
                self.courage += 25  # Big bonus for brave success
                self.health -= 15
                type_text("+25 Courage for incredible bravery!")
            else:
                type_text("\n❌ Too dangerous! You get injured.")
                type_text("But +5 Courage for trying something dangerous!")
                self.courage += 5  # Still get courage for trying
                self.health -= 25
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            return
    
    def heal_organic_fracture(self):
        """Heal the organic fracture."""
        clear_screen()
        print_scene_banner("ORGANIC FRACTURE")
        
        if self.organic_fixed:
            type_text("\nThis fracture is already healed.")
            input("\nPress Enter to continue...")
            return
        
        type_text("\nCrystalline vines are withering. Life energy fades.")
        
        print("\n" + "─" * 50)
        print("How will you heal it?")
        print("1. Use Time Sap (if you have it)")
        print("2. Use Lumina Blossom (if you have it)")
        print("3. Try compassionate healing (requires compassion)")
        print("4. Return to core chamber")
        
        choice = self.get_choice(["1", "2", "3", "4"])
        
        if choice == "1":
            if "Time Sap" in self.inventory:
                type_text("\nThe Time Sap revitalizes the vines!")
                type_text("✅ ORGANIC FRACTURE HEALED!")
                self.organic_fixed = True
                self.compassion += 20
                self.courage += 5  # Courage for success
                type_text("+5 Courage for healing nature!")
            else:
                type_text("\nYou don't have Time Sap.")
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            if "Lumina Blossom" in self.inventory:
                type_text("\nThe blossom's light heals the crystalline growth!")
                type_text("✅ ORGANIC FRACTURE HEALED!")
                self.organic_fixed = True
                self.compassion += 15
                self.courage += 5  # Courage for success
                type_text("+5 Courage for using magical items!")
            else:
                type_text("\nYou don't have the Lumina Blossom.")
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            type_text("\nYou try to heal with compassion...")
            type_text(f"Your compassion: {self.compassion}/50 needed")
            if self.compassion >= 50:
                type_text("\n✅ Your kindness resonates with the life force!")
                type_text("✅ ORGANIC FRACTURE HEALED!")
                self.organic_fixed = True
                self.compassion += 10
                self.courage += 15  # Big courage for emotional bravery
                type_text("+15 Courage for emotional strength!")
            else:
                type_text("\n❌ You lack the compassion needed.")
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            return
    
    def heal_elemental_fracture(self):
        """Heal the elemental fracture."""
        clear_screen()
        print_scene_banner("ELEMENTAL FRACTURE")
        
        if self.elemental_fixed:
            type_text("\nThis fracture is already healed.")
            input("\nPress Enter to continue...")
            return
        
        type_text("\nRaw temporal energy arcs dangerously. Reality is unstable.")
        
        print("\n" + "─" * 50)
        print("How will you heal it?")
        print("1. Use Crystal Chronicle (if you have it)")
        print("2. Use Heat Gloves (if you have them)")
        print("3. Try to contain energy (requires knowledge)")
        print("4. Return to core chamber")
        
        choice = self.get_choice(["1", "2", "3", "4"])
        
        if choice == "1":
            if "Crystal Chronicle" in self.inventory:
                type_text("\nThe Chronicle stabilizes the temporal energy!")
                type_text("✅ ELEMENTAL FRACTURE HEALED!")
                self.elemental_fixed = True
                self.knowledge += 25
                self.courage += 20  # Courage for facing raw energy
                type_text("+20 Courage for facing temporal chaos!")
            else:
                type_text("\nYou don't have the Crystal Chronicle.")
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            if "Heat Gloves" in self.inventory:
                type_text("\nThe gloves protect you as you channel the energy!")
                type_text("✅ ELEMENTAL FRACTURE HEALED!")
                self.elemental_fixed = True
                self.courage += 25  # Big courage bonus
                type_text("+25 Courage for channeling dangerous energy!")
            else:
                type_text("\nYou don't have Heat Gloves.")
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            type_text("\nYou attempt to contain the energy...")
            type_text(f"Your knowledge: {self.knowledge}/60 needed")
            if self.knowledge >= 60:
                type_text("\n✅ Your knowledge lets you stabilize the fracture!")
                type_text("✅ ELEMENTAL FRACTURE HEALED!")
                self.elemental_fixed = True
                self.knowledge += 15
                self.courage += 20  # Courage for intellectual bravery
                self.health -= 10
                type_text("+20 Courage for intellectual bravery!")
            else:
                type_text("\n❌ The energy is too complex for your understanding.")
                type_text("But +5 Courage for trying!")
                self.courage += 5
                self.health -= 20
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            return
    
    def check_robot(self):
        """Check the damaged robot."""
        clear_screen()
        print_scene_banner("DAMAGED ASSISTANT")
        
        if not self.helped_robot:
            type_text("\nA damaged robot sparks weakly.")
            type_text("It beeps: 'Core... failing... help...'")
            
            print("\n" + "─" * 50)
            print("Will you help the robot?")
            print("1. Yes, try to repair it (requires Oil Can)")
            print("2. No, focus on the core")
            
            choice = self.get_choice(["1", "2"])
            
            if choice == "1":
                if "Oil Can" in self.inventory:
                    type_text("\nYou use oil to repair the robot's joints!")
                    type_text("It thanks you and gives you a REPAIR MANUAL.")
                    self.inventory.append("Repair Manual")
                    self.helped_robot = True
                    self.compassion += 25
                    self.courage += 15  # Courage for helping
                    type_text("+25 Compassion, +15 Courage!")
                else:
                    type_text("\nYou lack the tools to repair it properly.")
            else:
                type_text("\nYou leave the robot as it is.")
        else:
            type_text("\nThe repaired robot hums happily.")
            type_text("'Thank you for your help, Timekeeper!'")
        
        input("\nPress Enter to continue...")
    
    def complete_chapter_2(self):
        """Complete Chapter 2."""
        clear_screen()
        print_banner("CHAPTER 2 COMPLETE!")
        
        type_text("\nAll three fractures are healed!")
        type_text("The Chrono-Core stabilizes at 100%!")
        type_text("Brilliant light fills the chamber...")
        
        # FIXED: Big courage bonus for completing Chapter 2
        type_text("\n🛡️  +30 COURAGE for restoring the Chrono-Core!")
        self.courage += 30
        
        input("\nPress Enter for the final choice...")
        self.current_chapter = 3
        self.final_choice()
    
    # ==================== FINAL CHAPTER ====================
    
    def final_choice(self):
        """Final choice that determines ending."""
        clear_screen()
        print_banner("FINAL CONVERGENCE")
        
        type_text("\nThe Chrono-Core is stable. Time itself asks for guidance.")
        type_text("How will you shape the future of time?")
        
        self.show_stats()
        print("\n" + "─" * 50)
        print("Choose the future:")
        print("1. ORDER - Perfect stability, no surprises")
        print("2. BALANCE - Harmony between change and stability")
        print("3. EVOLUTION - Constant change and growth")
        
        # Special ending if all stats are high
        if self.knowledge >= 70 and self.courage >= 70 and self.compassion >= 70:
            print("4. ENLIGHTENMENT - Become one with time (Secret Ending)")
            options = ["1", "2", "3", "4"]
        else:
            options = ["1", "2", "3"]
        
        choice = self.get_choice(options)
        
        if choice == "1":
            self.ending_order()
        elif choice == "2":
            self.ending_balance()
        elif choice == "3":
            self.ending_evolution()
        elif choice == "4":
            self.ending_enlightenment()
    
    # ==================== ENDINGS ====================
    
    def ending_order(self):
        """Order ending."""
        clear_screen()
        print_banner("ENDING: THE PERFECT CLOCK")
        
        type_text(f"\n{self.player_name}, you choose ORDER.")
        type_text("\nTime becomes a perfect, predictable mechanism.")
        type_text("Every second ticks with mathematical precision.")
        type_text("No surprises, no changes, no growth.")
        type_text("\nThe world is safe... but frozen.")
        type_text("You become the Keeper of the Eternal Clock.")
        
        self.ending = "ORDER ENDING: The Perfect Clock"
        self.show_ending_stats()
    
    def ending_balance(self):
        """Balance ending."""
        clear_screen()
        print_banner("ENDING: HARMONY RESTORED")
        
        type_text(f"\n{self.player_name}, you choose BALANCE.")
        type_text("\nTime flows naturally between order and change.")
        type_text("Seasons come and go, civilizations rise and fall.")
        type_text("Life finds its rhythm in the great dance of time.")
        
        if self.compassion >= 60 and self.helped_robot and self.saved_owl:
            type_text("\n✨ Because of your great compassion,")
            type_text("you achieve PERFECT HARMONY!")
            type_text("All beings thrive in your balanced time.")
            self.ending = "PERFECT ENDING: Master of Balance"
        else:
            type_text("\nBalance is restored. The world continues.")
            type_text("You have done well, Timekeeper.")
            self.ending = "GOOD ENDING: Harmony Restored"
        
        self.show_ending_stats()
    
    def ending_evolution(self):
        """Evolution ending."""
        clear_screen()
        print_banner("ENDING: RIVER OF CHANGE")
        
        type_text(f"\n{self.player_name}, you choose EVOLUTION.")
        type_text("\nTime becomes a rushing river of constant change.")
        type_text("Innovation accelerates, discoveries multiply!")
        
        if self.knowledge >= 70 and self.has_crystal_chronicle:
            type_text("\n🧠 Your wisdom guides the rapid changes.")
            type_text("A golden age of discovery begins under your watch!")
            self.ending = "EVOLUTION ENDING: Guided Progress"
        else:
            type_text("\nChange comes rapidly, sometimes chaotically.")
            type_text("The future is exciting but unpredictable...")
            self.ending = "CHAOTIC ENDING: Unchecked Evolution"
        
        self.show_ending_stats()
    
    def ending_enlightenment(self):
        """Secret enlightenment ending."""
        clear_screen()
        print_banner("ENDING: THE ENLIGHTENED")
        
        type_text(f"\n{self.player_name}, you achieve ENLIGHTENMENT.")
        type_text("\nYou understand: Time is not to be controlled.")
        type_text("It simply IS. You become one with time itself.")
        type_text("\nYou exist in every moment, everywhere.")
        type_text("Not controlling, but understanding. Not ruling, but being.")
        type_text("\nThis is the true purpose of a Timekeeper.")
        
        self.ending = "SECRET ENDING: The Enlightened"
        self.show_ending_stats()
    
    def game_over(self, reason):
        """Game over screen."""
        clear_screen()
        print_banner("GAME OVER")
        
        type_text(f"\n{self.player_name}, your journey ends here.")
        type_text(f"Reason: {reason}")
        type_text("\nTime continues without a keeper...")
        
        self.ending = f"GAME OVER: {reason}"
        self.show_ending_stats()
    
    def show_ending_stats(self):
        """Show final statistics."""
        time.sleep(2)
        clear_screen()
        print_banner("ADVENTURE COMPLETE")
        
        print("\n" + "=" * 60)
        print(f"HERO: {self.player_name}")
        print(f"ENDING: {self.ending}")
        print("=" * 60)
        
        print("\n📊 FINAL STATISTICS:")
        print(f"  ❤️  Health: {self.health}/100")
        print(f"  🧠 Knowledge: {self.knowledge}")
        print(f"  🛡️  Courage: {self.courage}")
        print(f"  ❤️  Compassion: {self.compassion}")
        
        print("\n🎒 INVENTORY:")
        if self.inventory:
            for item in self.inventory:
                print(f"  • {item}")
        else:
            print("  (Empty)")
        
        print("\n🌟 ACHIEVEMENTS:")
        achievements = []
        if self.saved_owl: achievements.append("✓ Saved the Mechanical Owl")
        if self.has_time_sap: achievements.append("✓ Healed the Crystal Tree")
        if self.has_temporal_hammer: achievements.append("✓ Forged Temporal Hammer")
        if self.helped_robot: achievements.append("✓ Repaired the Assistant Robot")
        if self.mechanical_fixed: achievements.append("✓ Healed Mechanical Fracture")
        if self.organic_fixed: achievements.append("✓ Healed Organic Fracture")
        if self.elemental_fixed: achievements.append("✓ Healed Elemental Fracture")
        
        if achievements:
            for ach in achievements:
                print(f"  {ach}")
        else:
            print("  (No achievements)")
        
        print("\n" + "=" * 60)
        
        # Play again option
        print("\nWould you like to:")
        print("1. Play Again")
        print("2. Exit Game")
        
        choice = self.get_choice(["1", "2"])
        
        if choice == "1":
            self.__init__()
            self.start_game()
        else:
            clear_screen()
            print_banner("THANK YOU FOR PLAYING!")
            type_text("\nCreated by Himanshu Choudhari")
            type_text("For Python Project Presentation")
            time.sleep(3)
            exit()

def main():
    """Main game launcher."""
    while True:
        clear_screen()
        print_banner("TIMEKEEPER CHRONICLES")
        print("\n" + "=" * 60)
        print("1. 🎮 Start New Game")
        print("2. 📖 How to Play")
        print("3. 🚪 Exit")
        print("=" * 60)
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == "1":
            game = TimekeeperChronicles()
            game.start_game()
        elif choice == "2":
            clear_screen()
            print_banner("HOW TO PLAY")
            print("\n🎯 OBJECTIVE:")
            print("  Restore the Chrono-Core and choose time's future")
            print("\n🎮 CONTROLS:")
            print("  • Type numbers to make choices")
            print("  • Collect items to solve puzzles")
            print("  • Manage your stats (Health, Knowledge, Courage, Compassion)")
            print("\n🌟 TIPS:")
            print("  • Explore all areas in Chapter 1")
            print("  • Help characters you meet")
            print("  • Different stats unlock different choices")
            print("  • Your choices determine the ending")
            print("\n💪 COURAGE TIPS:")
            print("  • Enter Volcanic area: +15 Courage")
            print("  • Enter Mechanical area: +10 Courage")
            print("  • Try dangerous actions: +5-25 Courage")
            print("  • Complete chapters: +20-30 Courage")
            input("\nPress Enter to return to menu...")
        elif choice == "3":
            clear_screen()
            print_banner("GOODBYE!")
            type_text("\nMay your time be well spent!")
            time.sleep(2)
            break

# Start the game
if __name__ == "__main__":
    main()