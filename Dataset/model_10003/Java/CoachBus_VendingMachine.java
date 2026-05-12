





import java.util.List;
import java.util.ArrayList;

public class CoachBus_VendingMachine  {

    private int number;





    private CoachBus_BookingOffice coachbus_bookingoffice;




    private CoachBus_BookingOffice coachbus_bookingoffice;




    private List<CoachBus_Ticket> coachbus_tickets;




    private CoachBus_Ticket coachbus_ticket;


    public CoachBus_VendingMachine(
        int number    ) {
        this.number = number;
        this.coachbus_tickets = new ArrayList<>();
    }

    public CoachBus_VendingMachine(
        int number        ArrayList<CoachBus_Ticket> coachbus_tickets    ) {
        this.number = number;
        this.coachbus_tickets = coachbus_tickets;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public CoachBus_BookingOffice getCoachbus_bookingoffice() {
        return coachbus_bookingoffice;
    }

    public void setCoachbus_bookingoffice(CoachBus_BookingOffice coachbus_bookingoffice) {
        this.coachbus_bookingoffice = coachbus_bookingoffice;
    }
    public CoachBus_BookingOffice getCoachbus_bookingoffice() {
        return coachbus_bookingoffice;
    }

    public void setCoachbus_bookingoffice(CoachBus_BookingOffice coachbus_bookingoffice) {
        this.coachbus_bookingoffice = coachbus_bookingoffice;
    }
    public List<CoachBus_Ticket> getCoachbus_tickets() {
        return coachbus_tickets;
    }

    public void addCoachbus_ticket(Coachbus_ticket coachbus_ticket) {
        this.coachbus_tickets.add(coachbus_ticket);
    }
    public CoachBus_Ticket getCoachbus_ticket() {
        return coachbus_ticket;
    }

    public void setCoachbus_ticket(CoachBus_Ticket coachbus_ticket) {
        this.coachbus_ticket = coachbus_ticket;
    }

}