





import java.util.List;
import java.util.ArrayList;

public class micro_Operation extends NamedElement {

    private String operationType;
    private boolean isMethodController;





    private micro_Model micro_model;




    private micro_Saga micro_saga;


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

    public micro_Model getMicro_model() {
        return micro_model;
    }

    public void setMicro_model(micro_Model micro_model) {
        this.micro_model = micro_model;
    }
    public micro_Saga getMicro_saga() {
        return micro_saga;
    }

    public void setMicro_saga(micro_Saga micro_saga) {
        this.micro_saga = micro_saga;
    }

}