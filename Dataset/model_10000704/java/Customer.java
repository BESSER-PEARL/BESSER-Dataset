





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String email;
    private int phoneNumber;
    private String ident;
    private int roomID;
    private String name;



    public Customer(
        String email,        int phoneNumber,        String ident,        int roomID,        String name    ) {
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.ident = ident;
        this.roomID = roomID;
        this.name = name;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getIdent() {
        return ident;
    }

    public void setIdent(String ident) {
        this.ident = ident;
    }
    public int getRoomid() {
        return roomID;
    }

    public void setRoomid(int roomID) {
        this.roomID = roomID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}