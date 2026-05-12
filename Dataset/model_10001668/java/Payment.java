





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String discountamount;
    private int quantity;
    private int ID;
    private String Imtiaz;
    private String finalamount;
    private String amount__;
    private String totalamount;
    private String list;





    private Customer customer;


    public Payment(
        String discountamount,        int quantity,        int ID,        String Imtiaz,        String finalamount,        String amount__,        String totalamount,        String list    ) {
        this.discountamount = discountamount;
        this.quantity = quantity;
        this.ID = ID;
        this.Imtiaz = Imtiaz;
        this.finalamount = finalamount;
        this.amount__ = amount__;
        this.totalamount = totalamount;
        this.list = list;
    }


    public String getDiscountamount() {
        return discountamount;
    }

    public void setDiscountamount(String discountamount) {
        this.discountamount = discountamount;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getImtiaz() {
        return Imtiaz;
    }

    public void setImtiaz(String Imtiaz) {
        this.Imtiaz = Imtiaz;
    }
    public String getFinalamount() {
        return finalamount;
    }

    public void setFinalamount(String finalamount) {
        this.finalamount = finalamount;
    }
    public String getAmount__() {
        return amount__;
    }

    public void setAmount__(String amount__) {
        this.amount__ = amount__;
    }
    public String getTotalamount() {
        return totalamount;
    }

    public void setTotalamount(String totalamount) {
        this.totalamount = totalamount;
    }
    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}