





import java.util.List;
import java.util.ArrayList;

public class ocl_type_EMessageType extends EClassifier {

    private String referredOperation;



    public ocl_type_EMessageType(
        String referredOperation    ) {
        super(
        );
        this.referredOperation = referredOperation;
    }


    public String getReferredoperation() {
        return referredOperation;
    }

    public void setReferredoperation(String referredOperation) {
        this.referredOperation = referredOperation;
    }


}