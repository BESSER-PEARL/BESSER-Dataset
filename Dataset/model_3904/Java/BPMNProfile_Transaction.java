





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Transaction extends SubProcess {

    private String method;



    public BPMNProfile_Transaction(
        String method    ) {
        super(
        );
        this.method = method;
    }


    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }


}