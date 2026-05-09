





import java.util.List;
import java.util.ArrayList;

public class UMLModel_InvocationAction extends Action {

    private String onPort;



    public UMLModel_InvocationAction(
        String onPort    ) {
        super(
        );
        this.onPort = onPort;
    }


    public String getOnport() {
        return onPort;
    }

    public void setOnport(String onPort) {
        this.onPort = onPort;
    }


}