





import java.util.List;
import java.util.ArrayList;

public class micro_Operation extends NamedElement {

    private String operationType;
    private boolean isMethodController;



    public micro_Operation(
        String operationType,        boolean isMethodController    ) {
        super(
        );
        this.operationType = operationType;
        this.isMethodController = isMethodController;
    }


    public String getOperationtype() {
        return operationType;
    }

    public void setOperationtype(String operationType) {
        this.operationType = operationType;
    }
    public boolean getIsmethodcontroller() {
        return isMethodController;
    }

    public void setIsmethodcontroller(boolean isMethodController) {
        this.isMethodController = isMethodController;
    }


}