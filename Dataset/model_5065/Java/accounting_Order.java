





import java.util.List;
import java.util.ArrayList;

public class accounting_Order  {

    private String id;
    private float pricePerUnit;
    private int paymentOffset;



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


}