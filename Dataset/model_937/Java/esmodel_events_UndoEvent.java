





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_UndoEvent extends Event {






    private operations_AbstractOperation operations_abstractoperation;


    public esmodel_events_UndoEvent(
    ) {
        super(
        );
    }



    public operations_AbstractOperation getOperations_abstractoperation() {
        return operations_abstractoperation;
    }

    public void setOperations_abstractoperation(operations_AbstractOperation operations_abstractoperation) {
        this.operations_abstractoperation = operations_abstractoperation;
    }

}