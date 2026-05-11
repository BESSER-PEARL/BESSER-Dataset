





import java.util.List;
import java.util.ArrayList;

public class componentModel_OutPort extends Port {






    private componentModel_CompConnDec componentmodel_compconndec;




    private componentModel_SystemPortOut componentmodel_systemportout;


    public componentModel_OutPort(
    ) {
        super(
        );
    }



    public componentModel_CompConnDec getComponentmodel_compconndec() {
        return componentmodel_compconndec;
    }

    public void setComponentmodel_compconndec(componentModel_CompConnDec componentmodel_compconndec) {
        this.componentmodel_compconndec = componentmodel_compconndec;
    }
    public componentModel_SystemPortOut getComponentmodel_systemportout() {
        return componentmodel_systemportout;
    }

    public void setComponentmodel_systemportout(componentModel_SystemPortOut componentmodel_systemportout) {
        this.componentmodel_systemportout = componentmodel_systemportout;
    }

}