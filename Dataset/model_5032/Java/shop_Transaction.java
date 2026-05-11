




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class shop_Transaction  {

    private LocalDate endDate;
    private LocalDate startDate;
    private LocalDate paidDate;
    private String number;
    private float price;





    private shop_Order shop_order;




    private shop_Order shop_order;




    private shop_Product shop_product;


    public shop_Transaction(
        LocalDate endDate,        LocalDate startDate,        LocalDate paidDate,        String number,        float price    ) {
        this.endDate = endDate;
        this.startDate = startDate;
        this.paidDate = paidDate;
        this.number = number;
        this.price = price;
    }


    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getPaiddate() {
        return paidDate;
    }

    public void setPaiddate(LocalDate paidDate) {
        this.paidDate = paidDate;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public shop_Order getShop_order() {
        return shop_order;
    }

    public void setShop_order(shop_Order shop_order) {
        this.shop_order = shop_order;
    }
    public shop_Order getShop_order() {
        return shop_order;
    }

    public void setShop_order(shop_Order shop_order) {
        this.shop_order = shop_order;
    }
    public shop_Product getShop_product() {
        return shop_product;
    }

    public void setShop_product(shop_Product shop_product) {
        this.shop_product = shop_product;
    }

}