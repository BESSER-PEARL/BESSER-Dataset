





import java.util.List;
import java.util.ArrayList;

public class spem_WorkProductPort extends ProcessElement {

    private boolean isOptional;
    private String portKind;





    private spem_WorkProductDefinition spem_workproductdefinition;


    public spem_WorkProductPort(
        boolean isOptional,        String portKind    ) {
        super(
        );
        this.isOptional = isOptional;
        this.portKind = portKind;
    }


    public boolean getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(boolean isOptional) {
        this.isOptional = isOptional;
    }
    public String getPortkind() {
        return portKind;
    }

    public void setPortkind(String portKind) {
        this.portKind = portKind;
    }

    public spem_WorkProductDefinition getSpem_workproductdefinition() {
        return spem_workproductdefinition;
    }

    public void setSpem_workproductdefinition(spem_WorkProductDefinition spem_workproductdefinition) {
        this.spem_workproductdefinition = spem_workproductdefinition;
    }

}