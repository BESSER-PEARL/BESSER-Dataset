





import java.util.List;
import java.util.ArrayList;

public class sipme_EnterpriseService extends EnterpriseObject {

    private String serviceState;



    public sipme_EnterpriseService(
        String serviceState    ) {
        super(
        );
        this.serviceState = serviceState;
    }


    public String getServicestate() {
        return serviceState;
    }

    public void setServicestate(String serviceState) {
        this.serviceState = serviceState;
    }


}