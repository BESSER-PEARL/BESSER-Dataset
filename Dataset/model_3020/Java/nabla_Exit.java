





import java.util.List;
import java.util.ArrayList;

public class nabla_Exit extends Instruction {

    private String message;



    public nabla_Exit(
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