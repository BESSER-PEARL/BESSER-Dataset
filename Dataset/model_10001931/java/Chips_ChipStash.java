





import java.util.List;
import java.util.ArrayList;

public class Chips_ChipStash  {






    private List<Chips_Chip> chips_chips;


    public Chips_ChipStash(
    ) {
        this.chips_chips = new ArrayList<>();
    }

    public Chips_ChipStash(
        ArrayList<Chips_Chip> chips_chips    ) {
        this.chips_chips = chips_chips;
    }


    public List<Chips_Chip> getChips_chips() {
        return chips_chips;
    }

    public void addChips_chip(Chips_chip chips_chip) {
        this.chips_chips.add(chips_chip);
    }

}