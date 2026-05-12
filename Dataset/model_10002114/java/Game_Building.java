





import java.util.List;
import java.util.ArrayList;

public class Game_Building  {

    private None ColonistZones;
    private int Cost;
    private String Type;
    private int MaxColonists;
    private boolean HasProduced;
    private int Size;
    private int VictoryPoints;



    public Game_Building(
        None ColonistZones,        int Cost,        String Type,        int MaxColonists,        boolean HasProduced,        int Size,        int VictoryPoints    ) {
        this.ColonistZones = ColonistZones;
        this.Cost = Cost;
        this.Type = Type;
        this.MaxColonists = MaxColonists;
        this.HasProduced = HasProduced;
        this.Size = Size;
        this.VictoryPoints = VictoryPoints;
    }


    public None getColonistzones() {
        return ColonistZones;
    }

    public void setColonistzones(None ColonistZones) {
        this.ColonistZones = ColonistZones;
    }
    public int getCost() {
        return Cost;
    }

    public void setCost(int Cost) {
        this.Cost = Cost;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public int getMaxcolonists() {
        return MaxColonists;
    }

    public void setMaxcolonists(int MaxColonists) {
        this.MaxColonists = MaxColonists;
    }
    public boolean getHasproduced() {
        return HasProduced;
    }

    public void setHasproduced(boolean HasProduced) {
        this.HasProduced = HasProduced;
    }
    public int getSize() {
        return Size;
    }

    public void setSize(int Size) {
        this.Size = Size;
    }
    public int getVictorypoints() {
        return VictoryPoints;
    }

    public void setVictorypoints(int VictoryPoints) {
        this.VictoryPoints = VictoryPoints;
    }


}