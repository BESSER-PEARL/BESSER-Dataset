





import java.util.List;
import java.util.ArrayList;

public class accounting_Order  {

    private float pricePerUnit;
    private int paymentOffset;
    private String id;



    public accounting_Order(
        float pricePerUnit,        int paymentOffset,        String id    ) {
        this.pricePerUnit = pricePerUnit;
        this.paymentOffset = paymentOffset;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}