





import java.util.List;
import java.util.ArrayList;

public class junitresult_NegativeResult  {

    private String message;
    private String value;
    private String type;



    public junitresult_NegativeResult(
        String message,        String value,        String type    ) {
        this.message = message;
        this.value = value;
        this.type = type;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}