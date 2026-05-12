





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_VendingMachine  {

    private int number;





    private CoachBusWithEDataType_BookingOffice coachbuswithedatatype_bookingoffice;




    private CoachBusWithEDataType_Ticket coachbuswithedatatype_ticket;




    private List<CoachBusWithEDataType_Ticket> coachbuswithedatatype_tickets;




    private CoachBusWithEDataType_BookingOffice coachbuswithedatatype_bookingoffice;


    public CoachBusWithEDataType_VendingMachine(
        int number    ) {
        this.number = number;
        this.coachbuswithedatatype_tickets = new ArrayList<>();
    }

    public CoachBusWithEDataType_VendingMachine(
        int number        ArrayList<CoachBusWithEDataType_Ticket> coachbuswithedatatype_tickets    ) {
        this.number = number;
        this.coachbuswithedatatype_tickets = coachbuswithedatatype_tickets;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public CoachBusWithEDataType_BookingOffice getCoachbuswithedatatype_bookingoffice() {
        return coachbuswithedatatype_bookingoffice;
    }

    public void setCoachbuswithedatatype_bookingoffice(CoachBusWithEDataType_BookingOffice coachbuswithedatatype_bookingoffice) {
        this.coachbuswithedatatype_bookingoffice = coachbuswithedatatype_bookingoffice;
    }
    public CoachBusWithEDataType_Ticket getCoachbuswithedatatype_ticket() {
        return coachbuswithedatatype_ticket;
    }

    public void setCoachbuswithedatatype_ticket(CoachBusWithEDataType_Ticket coachbuswithedatatype_ticket) {
        this.coachbuswithedatatype_ticket = coachbuswithedatatype_ticket;
    }
    public List<CoachBusWithEDataType_Ticket> getCoachbuswithedatatype_tickets() {
        return coachbuswithedatatype_tickets;
    }

    public void addCoachbuswithedatatype_ticket(Coachbuswithedatatype_ticket coachbuswithedatatype_ticket) {
        this.coachbuswithedatatype_tickets.add(coachbuswithedatatype_ticket);
    }
    public CoachBusWithEDataType_BookingOffice getCoachbuswithedatatype_bookingoffice() {
        return coachbuswithedatatype_bookingoffice;
    }

    public void setCoachbuswithedatatype_bookingoffice(CoachBusWithEDataType_BookingOffice coachbuswithedatatype_bookingoffice) {
        this.coachbuswithedatatype_bookingoffice = coachbuswithedatatype_bookingoffice;
    }

}