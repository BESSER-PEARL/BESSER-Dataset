





import java.util.List;
import java.util.ArrayList;

public class Etunit_ErrorType  {

    private String type;
    private String mixed;
    private String message;



    public Etunit_ErrorType(
        String type,        String mixed,        String message    ) {
        this.type = type;
        this.mixed = mixed;
        this.message = message;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }


}