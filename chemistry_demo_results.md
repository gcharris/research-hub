# Chemistry Demo: Cortisol Biosensor Design

**Goal:** Demonstrate Edison's ability to perform chemical calculations and design materials, which goes beyond standard search results.
**Agent Used:** `JobNames.MOLECULES` (Phoenix)
**Query:** *I am designing a biosensor for Cortisol. Calculate its exact LogP and Water Solubility... Suggest 3 functional monomers for a Molecularly Imprinted Polymer (MIP).*

## Results

### 1. Physicochemical Properties
Calculated directly from the cortisol structure:
- **LogP**: `1.78` (Moderately hydrophobic)
- **Water Solubility (logS)**: `-5.12` (Very low solubility)

*Why this matters:* The moderate hydrophobicity suggests that the sensor surface should not be too hydrophilic, or cortisol won't partition well onto it. Standard search might give you a range from different papers, but here we calculated it for the exact structure.

### 2. Material Design for MIPs
The agent analyzed the chemical structure of Cortisol (specifically its ketone and hydroxyl groups) and suggested these monomers for creating a polymer web that binds to it:

1.  **Methacrylic acid (MAA)**: Forms strong hydrogen bonds with cortisol's functional groups.
2.  **Acrylamide**: A versatile monomer for creating polar interactions.
3.  **4-Vinylpyridine**: Provides basic nitrogen sites to interact with hydroxyl protons.

*Why this matters:* This is an **engineering design suggestion**. It analyzed the hydrogen-bonding potential of the target molecule and matched it with complementary plastic building blocks.
