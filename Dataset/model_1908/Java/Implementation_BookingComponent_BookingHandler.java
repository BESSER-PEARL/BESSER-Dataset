





import java.util.List;
import java.util.ArrayList;

public class Implementation_BookingComponent_BookingHandler extends BookingComponent_IBookingDecision, BookingComponent_IBookingAdministration, BookingComponent_IBookingInformation {






    private Implementation_RoomComponent_IRoomInformation implementation_roomcomponent_iroominformation;




    private Implementation_StaffComponent_IAuthentication implementation_staffcomponent_iauthentication;




    private Implementation_AdditionalServiceComponent_IEventManagement implementation_additionalservicecomponent_ieventmanagement;




    private Implementation_PaymentComponent_IPayment implementation_paymentcomponent_ipayment;




    private List<Implementation_BookingComponent_Booking> implementation_bookingcomponent_bookings;


    public Implementation_BookingComponent_BookingHandler(
    ) {
        super(
        );
        this.implementation_bookingcomponent_bookings = new ArrayList<>();
    }

    public Implementation_BookingComponent_BookingHandler(
        ArrayList<Implementation_BookingComponent_Booking> implementation_bookingcomponent_bookings    ) {
        this.implementation_bookingcomponent_bookings = implementation_bookingcomponent_bookings;
    }


    public Implementation_RoomComponent_IRoomInformation getImplementation_roomcomponent_iroominformation() {
        return implementation_roomcomponent_iroominformation;
    }

    public void setImplementation_roomcomponent_iroominformation(Implementation_RoomComponent_IRoomInformation implementation_roomcomponent_iroominformation) {
        this.implementation_roomcomponent_iroominformation = implementation_roomcomponent_iroominformation;
    }
    public Implementation_StaffComponent_IAuthentication getImplementation_staffcomponent_iauthentication() {
        return implementation_staffcomponent_iauthentication;
    }

    public void setImplementation_staffcomponent_iauthentication(Implementation_StaffComponent_IAuthentication implementation_staffcomponent_iauthentication) {
        this.implementation_staffcomponent_iauthentication = implementation_staffcomponent_iauthentication;
    }
    public Implementation_AdditionalServiceComponent_IEventManagement getImplementation_additionalservicecomponent_ieventmanagement() {
        return implementation_additionalservicecomponent_ieventmanagement;
    }

    public void setImplementation_additionalservicecomponent_ieventmanagement(Implementation_AdditionalServiceComponent_IEventManagement implementation_additionalservicecomponent_ieventmanagement) {
        this.implementation_additionalservicecomponent_ieventmanagement = implementation_additionalservicecomponent_ieventmanagement;
    }
    public Implementation_PaymentComponent_IPayment getImplementation_paymentcomponent_ipayment() {
        return implementation_paymentcomponent_ipayment;
    }

    public void setImplementation_paymentcomponent_ipayment(Implementation_PaymentComponent_IPayment implementation_paymentcomponent_ipayment) {
        this.implementation_paymentcomponent_ipayment = implementation_paymentcomponent_ipayment;
    }
    public List<Implementation_BookingComponent_Booking> getImplementation_bookingcomponent_bookings() {
        return implementation_bookingcomponent_bookings;
    }

    public void addImplementation_bookingcomponent_booking(Implementation_bookingcomponent_booking implementation_bookingcomponent_booking) {
        this.implementation_bookingcomponent_bookings.add(implementation_bookingcomponent_booking);
    }

}