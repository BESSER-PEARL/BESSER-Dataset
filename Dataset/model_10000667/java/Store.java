





import java.util.List;
import java.util.ArrayList;

public class Store  {

    private String Address;
    private int StoreID;
    private String Name;



    public Store(
        String Address,        int StoreID,        String Name    ) {
        this.Address = Address;
        this.StoreID = StoreID;
        this.Name = Name;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getStoreid() {
        return StoreID;
    }

    public void setStoreid(int StoreID) {
        this.StoreID = StoreID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}