





import java.util.List;
import java.util.ArrayList;

public class junitresult_NegativeResult  {

    private String type;
    private String value;
    private String message;



    public junitresult_NegativeResult(
        String type,        String value,        String message    ) {
        this.type = type;
        this.value = value;
        this.message = message;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }


}