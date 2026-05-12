





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String discountamount;
    private String list;
    private int ID;
    private String amount__;
    private int quantity;
    private String Imtiaz;
    private String totalamount;
    private String finalamount;





    private Customer customer;


    public Payment(
        String discountamount,        String list,        int ID,        String amount__,        int quantity,        String Imtiaz,        String totalamount,        String finalamount    ) {
        this.discountamount = discountamount;
        this.list = list;
        this.ID = ID;
        this.amount__ = amount__;
        this.quantity = quantity;
        this.Imtiaz = Imtiaz;
        this.totalamount = totalamount;
        this.finalamount = finalamount;
    }


    public String getDiscountamount() {
        return discountamount;
    }

    public void setDiscountamount(String discountamount) {
        this.discountamount = discountamount;
    }
    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getAmount__() {
        return amount__;
    }

    public void setAmount__(String amount__) {
        this.amount__ = amount__;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getImtiaz() {
        return Imtiaz;
    }

    public void setImtiaz(String Imtiaz) {
        this.Imtiaz = Imtiaz;
    }
    public String getTotalamount() {
        return totalamount;
    }

    public void setTotalamount(String totalamount) {
        this.totalamount = totalamount;
    }
    public String getFinalamount() {
        return finalamount;
    }

    public void setFinalamount(String finalamount) {
        this.finalamount = finalamount;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}