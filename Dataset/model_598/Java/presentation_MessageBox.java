





import java.util.List;
import java.util.ArrayList;

public class presentation_MessageBox extends Dialog {

    private String message;



    public presentation_MessageBox(
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