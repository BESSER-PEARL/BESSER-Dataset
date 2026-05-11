





import java.util.List;
import java.util.ArrayList;

public class amazoninformational_Customer  {

    private boolean inGoodStanding;
    private float creditLimit;
    private String address;
    private boolean isVIP;
    private float consummedCredit;





    private amazoninformational_Order amazoninformational_order;


    public amazoninformational_Customer(
        boolean inGoodStanding,        float creditLimit,        String address,        boolean isVIP,        float consummedCredit    ) {
        this.inGoodStanding = inGoodStanding;
        this.creditLimit = creditLimit;
        this.address = address;
        this.isVIP = isVIP;
        this.consummedCredit = consummedCredit;
    }


    public boolean getIngoodstanding() {
        return inGoodStanding;
    }

    public void setIngoodstanding(boolean inGoodStanding) {
        this.inGoodStanding = inGoodStanding;
    }
    public float getCreditlimit() {
        return creditLimit;
    }

    public void setCreditlimit(float creditLimit) {
        this.creditLimit = creditLimit;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public boolean getIsvip() {
        return isVIP;
    }

    public void setIsvip(boolean isVIP) {
        this.isVIP = isVIP;
    }
    public float getConsummedcredit() {
        return consummedCredit;
    }

    public void setConsummedcredit(float consummedCredit) {
        this.consummedCredit = consummedCredit;
    }

    public amazoninformational_Order getAmazoninformational_order() {
        return amazoninformational_order;
    }

    public void setAmazoninformational_order(amazoninformational_Order amazoninformational_order) {
        this.amazoninformational_order = amazoninformational_order;
    }

}