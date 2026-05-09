





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Booking_PurchasedService  {

    private float price;
    private String name;





    private ClassDiagram_Booking_Bill classdiagram_booking_bill;


    public ClassDiagram_Booking_PurchasedService(
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

    public ClassDiagram_Booking_Bill getClassdiagram_booking_bill() {
        return classdiagram_booking_bill;
    }

    public void setClassdiagram_booking_bill(ClassDiagram_Booking_Bill classdiagram_booking_bill) {
        this.classdiagram_booking_bill = classdiagram_booking_bill;
    }

}