





import java.util.List;
import java.util.ArrayList;

public class shr5_ShoppingTransaction extends CredstickTransaction {

    private String caculatedCosts;
    private float fee;



    public shr5_ShoppingTransaction(
        String caculatedCosts,        float fee    ) {
        super(
        );
        this.caculatedCosts = caculatedCosts;
        this.fee = fee;
    }


    public String getCaculatedcosts() {
        return caculatedCosts;
    }

    public void setCaculatedcosts(String caculatedCosts) {
        this.caculatedCosts = caculatedCosts;
    }
    public float getFee() {
        return fee;
    }

    public void setFee(float fee) {
        this.fee = fee;
    }


}