





import java.util.List;
import java.util.ArrayList;

public class Reservation  {

    private int reservedSeats;
    private None user;
    private String uid;
    private None route;
    private int paymentMethod;
    private int reservationState;
    private boolean inCar;
    private String dueAmout;
    private None pickupLocation;
    private boolean reachedDest;
    private boolean paid;



    public Reservation(
        int reservedSeats,        None user,        String uid,        None route,        int paymentMethod,        int reservationState,        boolean inCar,        String dueAmout,        None pickupLocation,        boolean reachedDest,        boolean paid    ) {
        this.reservedSeats = reservedSeats;
        this.user = user;
        this.uid = uid;
        this.route = route;
        this.paymentMethod = paymentMethod;
        this.reservationState = reservationState;
        this.inCar = inCar;
        this.dueAmout = dueAmout;
        this.pickupLocation = pickupLocation;
        this.reachedDest = reachedDest;
        this.paid = paid;
    }


    public int getReservedseats() {
        return reservedSeats;
    }

    public void setReservedseats(int reservedSeats) {
        this.reservedSeats = reservedSeats;
    }
    public None getUser() {
        return user;
    }

    public void setUser(None user) {
        this.user = user;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public None getRoute() {
        return route;
    }

    public void setRoute(None route) {
        this.route = route;
    }
    public int getPaymentmethod() {
        return paymentMethod;
    }

    public void setPaymentmethod(int paymentMethod) {
        this.paymentMethod = paymentMethod;
    }
    public int getReservationstate() {
        return reservationState;
    }

    public void setReservationstate(int reservationState) {
        this.reservationState = reservationState;
    }
    public boolean getIncar() {
        return inCar;
    }

    public void setIncar(boolean inCar) {
        this.inCar = inCar;
    }
    public String getDueamout() {
        return dueAmout;
    }

    public void setDueamout(String dueAmout) {
        this.dueAmout = dueAmout;
    }
    public None getPickuplocation() {
        return pickupLocation;
    }

    public void setPickuplocation(None pickupLocation) {
        this.pickupLocation = pickupLocation;
    }
    public boolean getReacheddest() {
        return reachedDest;
    }

    public void setReacheddest(boolean reachedDest) {
        this.reachedDest = reachedDest;
    }
    public boolean getPaid() {
        return paid;
    }

    public void setPaid(boolean paid) {
        this.paid = paid;
    }


}