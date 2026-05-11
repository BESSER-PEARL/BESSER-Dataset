





import java.util.List;
import java.util.ArrayList;

public class aggregator_Status  {

    private String message;
    private String code;



    public aggregator_Status(
        String message,        String code    ) {
        this.message = message;
        this.code = code;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}