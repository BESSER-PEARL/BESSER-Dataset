





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Facility_FacilityService  {

    private float price;
    private String name;





    private ClassDiagram_Booking_BookedService classdiagram_booking_bookedservice;


    public ClassDiagram_Facility_FacilityService(
        float price,        String name    ) {
        this.price = price;
        this.name = name;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassDiagram_Booking_BookedService getClassdiagram_booking_bookedservice() {
        return classdiagram_booking_bookedservice;
    }

    public void setClassdiagram_booking_bookedservice(ClassDiagram_Booking_BookedService classdiagram_booking_bookedservice) {
        this.classdiagram_booking_bookedservice = classdiagram_booking_bookedservice;
    }

}