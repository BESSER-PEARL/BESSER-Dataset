





import java.util.List;
import java.util.ArrayList;

public class Items  {

    private int ItemID;
    private String Name;



    public Items(
        int ItemID,        String Name    ) {
        this.ItemID = ItemID;
        this.Name = Name;
    }


    public int getItemid() {
        return ItemID;
    }

    public void setItemid(int ItemID) {
        this.ItemID = ItemID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}