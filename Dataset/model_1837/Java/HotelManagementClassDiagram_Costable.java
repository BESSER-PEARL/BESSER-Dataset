





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Costable  {

    private float price;





    private HotelManagementClassDiagram_Bill hotelmanagementclassdiagram_bill;




    private List<HotelManagementClassDiagram_Discount> hotelmanagementclassdiagram_discounts;


    public HotelManagementClassDiagram_Costable(
        float price    ) {
        this.price = price;
        this.hotelmanagementclassdiagram_discounts = new ArrayList<>();
    }

    public HotelManagementClassDiagram_Costable(
        float price        ArrayList<HotelManagementClassDiagram_Discount> hotelmanagementclassdiagram_discounts    ) {
        this.price = price;
        this.hotelmanagementclassdiagram_discounts = hotelmanagementclassdiagram_discounts;
    }

    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public HotelManagementClassDiagram_Bill getHotelmanagementclassdiagram_bill() {
        return hotelmanagementclassdiagram_bill;
    }

    public void setHotelmanagementclassdiagram_bill(HotelManagementClassDiagram_Bill hotelmanagementclassdiagram_bill) {
        this.hotelmanagementclassdiagram_bill = hotelmanagementclassdiagram_bill;
    }
    public List<HotelManagementClassDiagram_Discount> getHotelmanagementclassdiagram_discounts() {
        return hotelmanagementclassdiagram_discounts;
    }

    public void addHotelmanagementclassdiagram_discount(Hotelmanagementclassdiagram_discount hotelmanagementclassdiagram_discount) {
        this.hotelmanagementclassdiagram_discounts.add(hotelmanagementclassdiagram_discount);
    }

}