





import java.util.List;
import java.util.ArrayList;

public class Guest  {

    private int phoneNo;
    private int id;
    private String Address;
    private int credit_card;
    private int Room;
    private String name;



    public Guest(
        int phoneNo,        int id,        String Address,        int credit_card,        int Room,        String name    ) {
        this.phoneNo = phoneNo;
        this.id = id;
        this.Address = Address;
        this.credit_card = credit_card;
        this.Room = Room;
        this.name = name;
    }


    public int getPhoneno() {
        return phoneNo;
    }

    public void setPhoneno(int phoneNo) {
        this.phoneNo = phoneNo;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getCredit_card() {
        return credit_card;
    }

    public void setCredit_card(int credit_card) {
        this.credit_card = credit_card;
    }
    public int getRoom() {
        return Room;
    }

    public void setRoom(int Room) {
        this.Room = Room;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}