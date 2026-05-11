





import java.util.List;
import java.util.ArrayList;

public class amazoninformational_Product  {

    private int onHand;





    private amazoninformational_Package amazoninformational_package;




    private amazoninformational_Order amazoninformational_order;


    public amazoninformational_Product(
        int onHand    ) {
        this.onHand = onHand;
    }


    public int getOnhand() {
        return onHand;
    }

    public void setOnhand(int onHand) {
        this.onHand = onHand;
    }

    public amazoninformational_Package getAmazoninformational_package() {
        return amazoninformational_package;
    }

    public void setAmazoninformational_package(amazoninformational_Package amazoninformational_package) {
        this.amazoninformational_package = amazoninformational_package;
    }
    public amazoninformational_Order getAmazoninformational_order() {
        return amazoninformational_order;
    }

    public void setAmazoninformational_order(amazoninformational_Order amazoninformational_order) {
        this.amazoninformational_order = amazoninformational_order;
    }

}