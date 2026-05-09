





import java.util.List;
import java.util.ArrayList;

public class Classes_Buissnesslayer_Booking  {

    private String parkings;
    private int guest;
    private String startDate;
    private String endDate;
    private String payment;
    private boolean checkedIn;
    private int bookingID;
    private int nrOfGuests;
    private boolean paymentComplete;
    private boolean checkedOut;
    private String extras;





    private List<Room> rooms;




    private List<Room> rooms;


    public Classes_Buissnesslayer_Booking(
        String parkings,        int guest,        String startDate,        String endDate,        String payment,        boolean checkedIn,        int bookingID,        int nrOfGuests,        boolean paymentComplete,        boolean checkedOut,        String extras    ) {
        this.parkings = parkings;
        this.guest = guest;
        this.startDate = startDate;
        this.endDate = endDate;
        this.payment = payment;
        this.checkedIn = checkedIn;
        this.bookingID = bookingID;
        this.nrOfGuests = nrOfGuests;
        this.paymentComplete = paymentComplete;
        this.checkedOut = checkedOut;
        this.extras = extras;
        this.rooms = new ArrayList<>();
        this.rooms = new ArrayList<>();
    }

    public Classes_Buissnesslayer_Booking(
        String parkings,        int guest,        String startDate,        String endDate,        String payment,        boolean checkedIn,        int bookingID,        int nrOfGuests,        boolean paymentComplete,        boolean checkedOut,        String extras        ArrayList<Room> rooms,        ArrayList<Room> rooms    ) {
        this.parkings = parkings;
        this.guest = guest;
        this.startDate = startDate;
        this.endDate = endDate;
        this.payment = payment;
        this.checkedIn = checkedIn;
        this.bookingID = bookingID;
        this.nrOfGuests = nrOfGuests;
        this.paymentComplete = paymentComplete;
        this.checkedOut = checkedOut;
        this.extras = extras;
        this.rooms = rooms;
        this.rooms = rooms;
    }

    public String getParkings() {
        return parkings;
    }

    public void setParkings(String parkings) {
        this.parkings = parkings;
    }
    public int getGuest() {
        return guest;
    }

    public void setGuest(int guest) {
        this.guest = guest;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public String getPayment() {
        return payment;
    }

    public void setPayment(String payment) {
        this.payment = payment;
    }
    public boolean getCheckedin() {
        return checkedIn;
    }

    public void setCheckedin(boolean checkedIn) {
        this.checkedIn = checkedIn;
    }
    public int getBookingid() {
        return bookingID;
    }

    public void setBookingid(int bookingID) {
        this.bookingID = bookingID;
    }
    public int getNrofguests() {
        return nrOfGuests;
    }

    public void setNrofguests(int nrOfGuests) {
        this.nrOfGuests = nrOfGuests;
    }
    public boolean getPaymentcomplete() {
        return paymentComplete;
    }

    public void setPaymentcomplete(boolean paymentComplete) {
        this.paymentComplete = paymentComplete;
    }
    public boolean getCheckedout() {
        return checkedOut;
    }

    public void setCheckedout(boolean checkedOut) {
        this.checkedOut = checkedOut;
    }
    public String getExtras() {
        return extras;
    }

    public void setExtras(String extras) {
        this.extras = extras;
    }

    public List<Room> getRooms() {
        return rooms;
    }

    public void addRoom(Room room) {
        this.rooms.add(room);
    }
    public List<Room> getRooms() {
        return rooms;
    }

    public void addRoom(Room room) {
        this.rooms.add(room);
    }

}