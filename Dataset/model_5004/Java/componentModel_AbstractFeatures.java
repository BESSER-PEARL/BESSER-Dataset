





import java.util.List;
import java.util.ArrayList;

public class componentModel_AbstractFeatures  {

    private String name;





    private componentModel_SystemDec componentmodel_systemdec;


    public componentModel_AbstractFeatures(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public componentModel_SystemDec getComponentmodel_systemdec() {
        return componentmodel_systemdec;
    }

    public void setComponentmodel_systemdec(componentModel_SystemDec componentmodel_systemdec) {
        this.componentmodel_systemdec = componentmodel_systemdec;
    }

}