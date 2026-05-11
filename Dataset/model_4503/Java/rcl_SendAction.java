





import java.util.List;
import java.util.ArrayList;

public class rcl_SendAction extends Action {

    private String message;



    public rcl_SendAction(
        String message    ) {
        super(
        );
        this.message = message;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }


}