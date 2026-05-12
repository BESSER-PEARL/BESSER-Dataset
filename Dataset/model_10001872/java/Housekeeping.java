





import java.util.List;
import java.util.ArrayList;

public class Housekeeping  {

    private int hkID;
    private String branch;
    private String name;





    private Rooms rooms;


    public Housekeeping(
        int hkID,        String branch,        String name    ) {
        this.hkID = hkID;
        this.branch = branch;
        this.name = name;
    }


    public int getHkid() {
        return hkID;
    }

    public void setHkid(int hkID) {
        this.hkID = hkID;
    }
    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Rooms getRooms() {
        return rooms;
    }

    public void setRooms(Rooms rooms) {
        this.rooms = rooms;
    }

}