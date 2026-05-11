





import java.util.List;
import java.util.ArrayList;

public class raspirover_LogAction extends Action {

    private String message;



    public raspirover_LogAction(
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