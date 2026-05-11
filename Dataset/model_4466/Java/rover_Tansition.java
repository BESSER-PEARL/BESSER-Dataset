





import java.util.List;
import java.util.ArrayList;

public class rover_Tansition  {

    private String operationUsed;
    private String comparedQuantity;



    public rover_Tansition(
        String operationUsed,        String comparedQuantity    ) {
        this.operationUsed = operationUsed;
        this.comparedQuantity = comparedQuantity;
    }


    public String getOperationused() {
        return operationUsed;
    }

    public void setOperationused(String operationUsed) {
        this.operationUsed = operationUsed;
    }
    public String getComparedquantity() {
        return comparedQuantity;
    }

    public void setComparedquantity(String comparedQuantity) {
        this.comparedQuantity = comparedQuantity;
    }


}