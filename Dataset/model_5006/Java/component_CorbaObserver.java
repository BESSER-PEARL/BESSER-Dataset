





import java.util.List;
import java.util.ArrayList;

public class component_CorbaObserver extends IPropertyMap, IAdaptable {

    private String serviceProfile;
    private String servant;



    public component_CorbaObserver(
        String serviceProfile,        String servant    ) {
        super(
        );
        this.serviceProfile = serviceProfile;
        this.servant = servant;
    }


    public String getServiceprofile() {
        return serviceProfile;
    }

    public void setServiceprofile(String serviceProfile) {
        this.serviceProfile = serviceProfile;
    }
    public String getServant() {
        return servant;
    }

    public void setServant(String servant) {
        this.servant = servant;
    }


}