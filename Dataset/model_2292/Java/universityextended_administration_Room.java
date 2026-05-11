





import java.util.List;
import java.util.ArrayList;

public class universityextended_administration_Room  {

    private String building;
    private int floor;
    private int roomnumber;



    public universityextended_administration_Room(
        String building,        int floor,        int roomnumber    ) {
        this.building = building;
        this.floor = floor;
        this.roomnumber = roomnumber;
    }


    public String getBuilding() {
        return building;
    }

    public void setBuilding(String building) {
        this.building = building;
    }
    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }
    public int getRoomnumber() {
        return roomnumber;
    }

    public void setRoomnumber(int roomnumber) {
        this.roomnumber = roomnumber;
    }


}