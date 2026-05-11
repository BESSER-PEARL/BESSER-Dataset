





import java.util.List;
import java.util.ArrayList;

public class behavior_AbstractBehaviorModelGraph  {

    private String transactionType;



    public behavior_AbstractBehaviorModelGraph(
        String transactionType    ) {
        this.transactionType = transactionType;
    }


    public String getTransactiontype() {
        return transactionType;
    }

    public void setTransactiontype(String transactionType) {
        this.transactionType = transactionType;
    }


}