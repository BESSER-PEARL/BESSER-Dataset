





import java.util.List;
import java.util.ArrayList;

public class accounting_Order  {

    private String id;
    private float pricePerUnit;
    private int paymentOffset;





    private accounting_Project accounting_project;




    private accounting_Project accounting_project;


    public accounting_Order(
        String id,        float pricePerUnit,        int paymentOffset    ) {
        this.id = id;
        this.pricePerUnit = pricePerUnit;
        this.paymentOffset = paymentOffset;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public float getPriceperunit() {
        return pricePerUnit;
    }

    public void setPriceperunit(float pricePerUnit) {
        this.pricePerUnit = pricePerUnit;
    }
    public int getPaymentoffset() {
        return paymentOffset;
    }

    public void setPaymentoffset(int paymentOffset) {
        this.paymentOffset = paymentOffset;
    }

    public accounting_Project getAccounting_project() {
        return accounting_project;
    }

    public void setAccounting_project(accounting_Project accounting_project) {
        this.accounting_project = accounting_project;
    }
    public accounting_Project getAccounting_project() {
        return accounting_project;
    }

    public void setAccounting_project(accounting_Project accounting_project) {
        this.accounting_project = accounting_project;
    }

}