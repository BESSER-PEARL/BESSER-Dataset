





import java.util.List;
import java.util.ArrayList;

public class componentModel_Parameter extends SimpleParameterType {

    private String name;





    private componentModel_Signature componentmodel_signature;


    public componentModel_Parameter(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public componentModel_Signature getComponentmodel_signature() {
        return componentmodel_signature;
    }

    public void setComponentmodel_signature(componentModel_Signature componentmodel_signature) {
        this.componentmodel_signature = componentmodel_signature;
    }

}