





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private int billNo;
    private int guestID;





    private Guest guest;




    private List<Receptionist> receptionists;


    public Bill(
        int billNo,        int guestID    ) {
        this.billNo = billNo;
        this.guestID = guestID;
        this.receptionists = new ArrayList<>();
    }

    public Bill(
        int billNo,        int guestID        ArrayList<Receptionist> receptionists    ) {
        this.billNo = billNo;
        this.guestID = guestID;
        this.receptionists = receptionists;
    }

    public int getBillno() {
        return billNo;
    }

    public void setBillno(int billNo) {
        this.billNo = billNo;
    }
    public int getGuestid() {
        return guestID;
    }

    public void setGuestid(int guestID) {
        this.guestID = guestID;
    }

    public Guest getGuest() {
        return guest;
    }

    public void setGuest(Guest guest) {
        this.guest = guest;
    }
    public List<Receptionist> getReceptionists() {
        return receptionists;
    }

    public void addReceptionist(Receptionist receptionist) {
        this.receptionists.add(receptionist);
    }

}