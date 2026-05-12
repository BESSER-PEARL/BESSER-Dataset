





import java.util.List;
import java.util.ArrayList;

public class Game_Plantation  {

    private boolean HasProduced;
    private None ColonistZone;
    private None Type;



    public Game_Plantation(
        boolean HasProduced,        None ColonistZone,        None Type    ) {
        this.HasProduced = HasProduced;
        this.ColonistZone = ColonistZone;
        this.Type = Type;
    }


    public boolean getHasproduced() {
        return HasProduced;
    }

    public void setHasproduced(boolean HasProduced) {
        this.HasProduced = HasProduced;
    }
    public None getColonistzone() {
        return ColonistZone;
    }

    public void setColonistzone(None ColonistZone) {
        this.ColonistZone = ColonistZone;
    }
    public None getType() {
        return Type;
    }

    public void setType(None Type) {
        this.Type = Type;
    }


}