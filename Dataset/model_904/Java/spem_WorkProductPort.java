





import java.util.List;
import java.util.ArrayList;

public class spem_WorkProductPort extends ProcessElement {

    private String portKind;
    private boolean isOptional;





    private spem_WorkProductPortConnector spem_workproductportconnector;


    public spem_WorkProductPort(
        String portKind,        boolean isOptional    ) {
        super(
        );
        this.portKind = portKind;
        this.isOptional = isOptional;
    }


    public String getPortkind() {
        return portKind;
    }

    public void setPortkind(String portKind) {
        this.portKind = portKind;
    }
    public boolean getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(boolean isOptional) {
        this.isOptional = isOptional;
    }

    public spem_WorkProductPortConnector getSpem_workproductportconnector() {
        return spem_workproductportconnector;
    }

    public void setSpem_workproductportconnector(spem_WorkProductPortConnector spem_workproductportconnector) {
        this.spem_workproductportconnector = spem_workproductportconnector;
    }

}