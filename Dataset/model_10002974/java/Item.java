





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private String name;
    private int unitcost;
    private int pieceAvailable;



    public Item(
        String name,        int unitcost,        int pieceAvailable    ) {
        this.name = name;
        this.unitcost = unitcost;
        this.pieceAvailable = pieceAvailable;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getUnitcost() {
        return unitcost;
    }

    public void setUnitcost(int unitcost) {
        this.unitcost = unitcost;
    }
    public int getPieceavailable() {
        return pieceAvailable;
    }

    public void setPieceavailable(int pieceAvailable) {
        this.pieceAvailable = pieceAvailable;
    }


}