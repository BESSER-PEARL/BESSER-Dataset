





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Bill  {

    private boolean paid;
    private float valueAddedTax;
    private boolean final;
    private float totalPrice;





    private HotelManagementClassDiagram_Customer hotelmanagementclassdiagram_customer;


    public HotelManagementClassDiagram_Bill(
        boolean paid,        float valueAddedTax,        boolean final,        float totalPrice    ) {
        this.paid = paid;
        this.valueAddedTax = valueAddedTax;
        this.final = final;
        this.totalPrice = totalPrice;
    }


    public boolean getPaid() {
        return paid;
    }

    public void setPaid(boolean paid) {
        this.paid = paid;
    }
    public float getValueaddedtax() {
        return valueAddedTax;
    }

    public void setValueaddedtax(float valueAddedTax) {
        this.valueAddedTax = valueAddedTax;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public float getTotalprice() {
        return totalPrice;
    }

    public void setTotalprice(float totalPrice) {
        this.totalPrice = totalPrice;
    }

    public HotelManagementClassDiagram_Customer getHotelmanagementclassdiagram_customer() {
        return hotelmanagementclassdiagram_customer;
    }

    public void setHotelmanagementclassdiagram_customer(HotelManagementClassDiagram_Customer hotelmanagementclassdiagram_customer) {
        this.hotelmanagementclassdiagram_customer = hotelmanagementclassdiagram_customer;
    }

}