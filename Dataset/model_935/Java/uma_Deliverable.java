





import java.util.List;
import java.util.ArrayList;

public class uma_Deliverable extends WorkProduct {

    private String group3;
    private String deliveredWorkProduct;



    public uma_Deliverable(
        String group3,        String deliveredWorkProduct    ) {
        super(
        );
        this.group3 = group3;
        this.deliveredWorkProduct = deliveredWorkProduct;
    }


    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getDeliveredworkproduct() {
        return deliveredWorkProduct;
    }

    public void setDeliveredworkproduct(String deliveredWorkProduct) {
        this.deliveredWorkProduct = deliveredWorkProduct;
    }


}