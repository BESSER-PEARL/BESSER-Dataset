





import java.util.List;
import java.util.ArrayList;

public class Game_ColonistShip  {

    private int Num_Colonists;
    private None ColonistZone;



    public Game_ColonistShip(
        int Num_Colonists,        None ColonistZone    ) {
        this.Num_Colonists = Num_Colonists;
        this.ColonistZone = ColonistZone;
    }


    public int getNum_colonists() {
        return Num_Colonists;
    }

    public void setNum_colonists(int Num_Colonists) {
        this.Num_Colonists = Num_Colonists;
    }
    public None getColonistzone() {
        return ColonistZone;
    }

    public void setColonistzone(None ColonistZone) {
        this.ColonistZone = ColonistZone;
    }


}