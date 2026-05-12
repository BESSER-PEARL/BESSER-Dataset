





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private int pieceAvailable;
    private int unitcost;
    private String name;



    public Item(
        int pieceAvailable,        int unitcost,        String name    ) {
        this.pieceAvailable = pieceAvailable;
        this.unitcost = unitcost;
        this.name = name;
    }


    public int getPieceavailable() {
        return pieceAvailable;
    }

    public void setPieceavailable(int pieceAvailable) {
        this.pieceAvailable = pieceAvailable;
    }
    public int getUnitcost() {
        return unitcost;
    }

    public void setUnitcost(int unitcost) {
        this.unitcost = unitcost;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}