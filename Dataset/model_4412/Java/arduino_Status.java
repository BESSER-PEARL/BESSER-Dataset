





import java.util.List;
import java.util.ArrayList;

public class arduino_Status extends ModuleInstruction, Value {

    private boolean status;



    public arduino_Status(
        boolean status    ) {
        super(
        );
        this.status = status;
    }


    public boolean getStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }


}