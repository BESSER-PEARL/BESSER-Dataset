





import java.util.List;
import java.util.ArrayList;

public class eShop_Sale  {

    private int amount;
    private int id;
    private boolean paid;





    private eShop_SaleLine eshop_saleline;




    private eShop_Customer eshop_customer;




    private eShop_Customer eshop_customer;




    private List<eShop_SaleLine> eshop_salelines;


    public eShop_Sale(
        int amount,        int id,        boolean paid    ) {
        this.amount = amount;
        this.id = id;
        this.paid = paid;
        this.eshop_salelines = new ArrayList<>();
    }

    public eShop_Sale(
        int amount,        int id,        boolean paid        ArrayList<eShop_SaleLine> eshop_salelines    ) {
        this.amount = amount;
        this.id = id;
        this.paid = paid;
        this.eshop_salelines = eshop_salelines;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getPaid() {
        return paid;
    }

    public void setPaid(boolean paid) {
        this.paid = paid;
    }

    public eShop_SaleLine getEshop_saleline() {
        return eshop_saleline;
    }

    public void setEshop_saleline(eShop_SaleLine eshop_saleline) {
        this.eshop_saleline = eshop_saleline;
    }
    public eShop_Customer getEshop_customer() {
        return eshop_customer;
    }

    public void setEshop_customer(eShop_Customer eshop_customer) {
        this.eshop_customer = eshop_customer;
    }
    public eShop_Customer getEshop_customer() {
        return eshop_customer;
    }

    public void setEshop_customer(eShop_Customer eshop_customer) {
        this.eshop_customer = eshop_customer;
    }
    public List<eShop_SaleLine> getEshop_salelines() {
        return eshop_salelines;
    }

    public void addEshop_saleline(Eshop_saleline eshop_saleline) {
        this.eshop_salelines.add(eshop_saleline);
    }

}