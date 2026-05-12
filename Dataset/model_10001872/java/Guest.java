





import java.util.List;
import java.util.ArrayList;

public class Guest  {

    private String address;
    private int guestID;
    private String name;
    private int roomNo;
    private int phoneNo;





    private Manager manager;


    public Guest(
        String address,        int guestID,        String name,        int roomNo,        int phoneNo    ) {
        this.address = address;
        this.guestID = guestID;
        this.name = name;
        this.roomNo = roomNo;
        this.phoneNo = phoneNo;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getGuestid() {
        return guestID;
    }

    public void setGuestid(int guestID) {
        this.guestID = guestID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getRoomno() {
        return roomNo;
    }

    public void setRoomno(int roomNo) {
        this.roomNo = roomNo;
    }
    public int getPhoneno() {
        return phoneNo;
    }

    public void setPhoneno(int phoneNo) {
        this.phoneNo = phoneNo;
    }

    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }

}