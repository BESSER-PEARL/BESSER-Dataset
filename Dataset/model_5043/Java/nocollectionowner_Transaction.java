




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class nocollectionowner_Transaction  {

    private LocalDate paidDate;
    private String number;
    private LocalDate endDate;
    private LocalDate startDate;
    private float price;





    private nocollectionowner_Order nocollectionowner_order;




    private nocollectionowner_Order nocollectionowner_order;




    private nocollectionowner_Product nocollectionowner_product;


    public nocollectionowner_Transaction(
        LocalDate paidDate,        String number,        LocalDate endDate,        LocalDate startDate,        float price    ) {
        this.paidDate = paidDate;
        this.number = number;
        this.endDate = endDate;
        this.startDate = startDate;
        this.price = price;
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
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public nocollectionowner_Order getNocollectionowner_order() {
        return nocollectionowner_order;
    }

    public void setNocollectionowner_order(nocollectionowner_Order nocollectionowner_order) {
        this.nocollectionowner_order = nocollectionowner_order;
    }
    public nocollectionowner_Order getNocollectionowner_order() {
        return nocollectionowner_order;
    }

    public void setNocollectionowner_order(nocollectionowner_Order nocollectionowner_order) {
        this.nocollectionowner_order = nocollectionowner_order;
    }
    public nocollectionowner_Product getNocollectionowner_product() {
        return nocollectionowner_product;
    }

    public void setNocollectionowner_product(nocollectionowner_Product nocollectionowner_product) {
        this.nocollectionowner_product = nocollectionowner_product;
    }

}