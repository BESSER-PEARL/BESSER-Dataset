





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String GuestName;
    private int bill_No;





    private Guest guest;




    private List<Receptionist> receptionists;


    public Bill(
        String GuestName,        int bill_No    ) {
        this.GuestName = GuestName;
        this.bill_No = bill_No;
        this.receptionists = new ArrayList<>();
    }

    public Bill(
        String GuestName,        int bill_No        ArrayList<Receptionist> receptionists    ) {
        this.GuestName = GuestName;
        this.bill_No = bill_No;
        this.receptionists = receptionists;
    }

    public String getGuestname() {
        return GuestName;
    }

    public void setGuestname(String GuestName) {
        this.GuestName = GuestName;
    }
    public int getBill_no() {
        return bill_No;
    }

    public void setBill_no(int bill_No) {
        this.bill_No = bill_No;
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