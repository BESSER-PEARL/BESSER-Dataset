





import java.util.List;
import java.util.ArrayList;

public class RootElement_ServiceItem  {

    private String description;
    private String name;
    private String price;





    private RootElement_Booking rootelement_booking;


    public RootElement_ServiceItem(
        String description,        String name,        String price    ) {
        this.description = description;
        this.name = name;
        this.price = price;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public RootElement_Booking getRootelement_booking() {
        return rootelement_booking;
    }

    public void setRootelement_booking(RootElement_Booking rootelement_booking) {
        this.rootelement_booking = rootelement_booking;
    }

}