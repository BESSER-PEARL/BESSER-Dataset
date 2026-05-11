





import java.util.List;
import java.util.ArrayList;

public class componentModel_InPort extends Port {






    private componentModel_SystemPortIn componentmodel_systemportin;




    private componentModel_CompConnDec componentmodel_compconndec;


    public componentModel_InPort(
    ) {
        super(
        );
    }



    public componentModel_SystemPortIn getComponentmodel_systemportin() {
        return componentmodel_systemportin;
    }

    public void setComponentmodel_systemportin(componentModel_SystemPortIn componentmodel_systemportin) {
        this.componentmodel_systemportin = componentmodel_systemportin;
    }
    public componentModel_CompConnDec getComponentmodel_compconndec() {
        return componentmodel_compconndec;
    }

    public void setComponentmodel_compconndec(componentModel_CompConnDec componentmodel_compconndec) {
        this.componentmodel_compconndec = componentmodel_compconndec;
    }

}