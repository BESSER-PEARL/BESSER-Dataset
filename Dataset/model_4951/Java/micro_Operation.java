





import java.util.List;
import java.util.ArrayList;

public class micro_Operation extends NamedElement {

    private String operationType;
    private boolean isMethodController;





    private micro_Saga micro_saga;




    private micro_AggregateService micro_aggregateservice;




    private micro_AggregateService micro_aggregateservice;




    private micro_Event micro_event;


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

    public micro_Saga getMicro_saga() {
        return micro_saga;
    }

    public void setMicro_saga(micro_Saga micro_saga) {
        this.micro_saga = micro_saga;
    }
    public micro_AggregateService getMicro_aggregateservice() {
        return micro_aggregateservice;
    }

    public void setMicro_aggregateservice(micro_AggregateService micro_aggregateservice) {
        this.micro_aggregateservice = micro_aggregateservice;
    }
    public micro_AggregateService getMicro_aggregateservice() {
        return micro_aggregateservice;
    }

    public void setMicro_aggregateservice(micro_AggregateService micro_aggregateservice) {
        this.micro_aggregateservice = micro_aggregateservice;
    }
    public micro_Event getMicro_event() {
        return micro_event;
    }

    public void setMicro_event(micro_Event micro_event) {
        this.micro_event = micro_event;
    }

}