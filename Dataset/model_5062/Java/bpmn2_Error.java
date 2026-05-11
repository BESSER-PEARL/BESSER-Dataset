





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Error extends RootElement {

    private String name;
    private String errorCode;



    public bpmn2_Error(
        String name,        String errorCode    ) {
        super(
        );
        this.name = name;
        this.errorCode = errorCode;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getErrorcode() {
        return errorCode;
    }

    public void setErrorcode(String errorCode) {
        this.errorCode = errorCode;
    }


}