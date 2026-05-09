





import java.util.List;
import java.util.ArrayList;

public class uml_ReceiveOperationEvent extends MessageEvent {






    private uml_Operation uml_operation;


    public uml_ReceiveOperationEvent(
    ) {
        super(
        );
    }



    public uml_Operation getUml_operation() {
        return uml_operation;
    }

    public void setUml_operation(uml_Operation uml_operation) {
        this.uml_operation = uml_operation;
    }

}