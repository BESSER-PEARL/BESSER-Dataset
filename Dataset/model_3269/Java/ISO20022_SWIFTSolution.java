





import java.util.List;
import java.util.ArrayList;

public class ISO20022_SWIFTSolution extends MessageSet {

    private String serviceName;



    public ISO20022_SWIFTSolution(
        String serviceName    ) {
        super(
        );
        this.serviceName = serviceName;
    }


    public String getServicename() {
        return serviceName;
    }

    public void setServicename(String serviceName) {
        this.serviceName = serviceName;
    }


}