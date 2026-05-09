





import java.util.List;
import java.util.ArrayList;

public class se_hotelsystem_BookingHandler extends hotelsystem_IHotelReceptionistProvides, hotelsystem_IHotelCustomerProvides {

    private int nextBookingId;
    private int bookingCurrentlyCheckingOut;





    private hotelsystem_PaymentHandler hotelsystem_paymenthandler;




    private List<hotelsystem_Booking> hotelsystem_bookings;




    private hotelsystem_IRoomHandler hotelsystem_iroomhandler;


    public se_hotelsystem_BookingHandler(
        int nextBookingId,        int bookingCurrentlyCheckingOut    ) {
        super(
        );
        this.nextBookingId = nextBookingId;
        this.bookingCurrentlyCheckingOut = bookingCurrentlyCheckingOut;
        this.hotelsystem_bookings = new ArrayList<>();
    }

    public se_hotelsystem_BookingHandler(
        int nextBookingId,        int bookingCurrentlyCheckingOut        ArrayList<hotelsystem_Booking> hotelsystem_bookings    ) {
        this.nextBookingId = nextBookingId;
        this.bookingCurrentlyCheckingOut = bookingCurrentlyCheckingOut;
        this.hotelsystem_bookings = hotelsystem_bookings;
    }

    public int getNextbookingid() {
        return nextBookingId;
    }

    public void setNextbookingid(int nextBookingId) {
        this.nextBookingId = nextBookingId;
    }
    public int getBookingcurrentlycheckingout() {
        return bookingCurrentlyCheckingOut;
    }

    public void setBookingcurrentlycheckingout(int bookingCurrentlyCheckingOut) {
        this.bookingCurrentlyCheckingOut = bookingCurrentlyCheckingOut;
    }

    public hotelsystem_PaymentHandler getHotelsystem_paymenthandler() {
        return hotelsystem_paymenthandler;
    }

    public void setHotelsystem_paymenthandler(hotelsystem_PaymentHandler hotelsystem_paymenthandler) {
        this.hotelsystem_paymenthandler = hotelsystem_paymenthandler;
    }
    public List<hotelsystem_Booking> getHotelsystem_bookings() {
        return hotelsystem_bookings;
    }

    public void addHotelsystem_booking(Hotelsystem_booking hotelsystem_booking) {
        this.hotelsystem_bookings.add(hotelsystem_booking);
    }
    public hotelsystem_IRoomHandler getHotelsystem_iroomhandler() {
        return hotelsystem_iroomhandler;
    }

    public void setHotelsystem_iroomhandler(hotelsystem_IRoomHandler hotelsystem_iroomhandler) {
        this.hotelsystem_iroomhandler = hotelsystem_iroomhandler;
    }

}