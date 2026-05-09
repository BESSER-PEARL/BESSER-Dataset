





import java.util.List;
import java.util.ArrayList;

public class webapp_ServiceController extends Controller {

    private String endpoint;



    public webapp_ServiceController(
        String endpoint    ) {
        super(
        );
        this.endpoint = endpoint;
    }


    public String getEndpoint() {
        return endpoint;
    }

    public void setEndpoint(String endpoint) {
        this.endpoint = endpoint;
    }


}