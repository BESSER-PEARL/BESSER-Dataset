





import java.util.List;
import java.util.ArrayList;

public class Implementation_BookingComponent_RoomType  {

    private String cost;
    private String roomType;





    private Implementation_BookingComponent_Booking implementation_bookingcomponent_booking;


    public Implementation_BookingComponent_RoomType(
        String cost,        String roomType    ) {
        this.cost = cost;
        this.roomType = roomType;
    }


    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }
    public String getRoomtype() {
        return roomType;
    }

    public void setRoomtype(String roomType) {
        this.roomType = roomType;
    }

    public Implementation_BookingComponent_Booking getImplementation_bookingcomponent_booking() {
        return implementation_bookingcomponent_booking;
    }

    public void setImplementation_bookingcomponent_booking(Implementation_BookingComponent_Booking implementation_bookingcomponent_booking) {
        this.implementation_bookingcomponent_booking = implementation_bookingcomponent_booking;
    }

}