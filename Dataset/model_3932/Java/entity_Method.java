





import java.util.List;
import java.util.ArrayList;

public class entity_Method extends Member {

    private boolean isAbstract;





    private entity_Service entity_service;


    public entity_Method(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public entity_Service getEntity_service() {
        return entity_service;
    }

    public void setEntity_service(entity_Service entity_service) {
        this.entity_service = entity_service;
    }

}