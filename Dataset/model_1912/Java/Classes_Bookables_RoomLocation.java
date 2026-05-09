





import java.util.List;
import java.util.ArrayList;

public class Classes_Bookables_RoomLocation  {

    private String addtionalInfo;
    private String floor;



    public Classes_Bookables_RoomLocation(
        String addtionalInfo,        String floor    ) {
        this.addtionalInfo = addtionalInfo;
        this.floor = floor;
    }


    public String getAddtionalinfo() {
        return addtionalInfo;
    }

    public void setAddtionalinfo(String addtionalInfo) {
        this.addtionalInfo = addtionalInfo;
    }
    public String getFloor() {
        return floor;
    }

    public void setFloor(String floor) {
        this.floor = floor;
    }


}