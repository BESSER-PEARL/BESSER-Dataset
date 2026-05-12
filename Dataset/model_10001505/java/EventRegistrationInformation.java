





import java.util.List;
import java.util.ArrayList;

public class EventRegistrationInformation  {

    private String eventId;
    private boolean isPaid;
    private None passenger;
    private int numberOfSeats;
    private String uid;
    private int paymentMethod;
    private int state;



    public EventRegistrationInformation(
        String eventId,        boolean isPaid,        None passenger,        int numberOfSeats,        String uid,        int paymentMethod,        int state    ) {
        this.eventId = eventId;
        this.isPaid = isPaid;
        this.passenger = passenger;
        this.numberOfSeats = numberOfSeats;
        this.uid = uid;
        this.paymentMethod = paymentMethod;
        this.state = state;
    }


    public String getEventid() {
        return eventId;
    }

    public void setEventid(String eventId) {
        this.eventId = eventId;
    }
    public boolean getIspaid() {
        return isPaid;
    }

    public void setIspaid(boolean isPaid) {
        this.isPaid = isPaid;
    }
    public None getPassenger() {
        return passenger;
    }

    public void setPassenger(None passenger) {
        this.passenger = passenger;
    }
    public int getNumberofseats() {
        return numberOfSeats;
    }

    public void setNumberofseats(int numberOfSeats) {
        this.numberOfSeats = numberOfSeats;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public int getPaymentmethod() {
        return paymentMethod;
    }

    public void setPaymentmethod(int paymentMethod) {
        this.paymentMethod = paymentMethod;
    }
    public int getState() {
        return state;
    }

    public void setState(int state) {
        this.state = state;
    }


}