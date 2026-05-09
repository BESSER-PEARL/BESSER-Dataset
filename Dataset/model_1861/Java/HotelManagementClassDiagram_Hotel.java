





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Hotel  {

    private String address;
    private float rank;
    private String name;



    public HotelManagementClassDiagram_Hotel(
        String address,        float rank,        String name    ) {
        this.address = address;
        this.rank = rank;
        this.name = name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public float getRank() {
        return rank;
    }

    public void setRank(float rank) {
        this.rank = rank;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}