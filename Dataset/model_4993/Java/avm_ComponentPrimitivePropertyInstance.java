





import java.util.List;
import java.util.ArrayList;

public class avm_ComponentPrimitivePropertyInstance  {

    private String IDinComponentModel;





    private avm_ComponentInstance avm_componentinstance;


    public avm_ComponentPrimitivePropertyInstance(
        String IDinComponentModel    ) {
        this.IDinComponentModel = IDinComponentModel;
    }


    public String getIdincomponentmodel() {
        return IDinComponentModel;
    }

    public void setIdincomponentmodel(String IDinComponentModel) {
        this.IDinComponentModel = IDinComponentModel;
    }

    public avm_ComponentInstance getAvm_componentinstance() {
        return avm_componentinstance;
    }

    public void setAvm_componentinstance(avm_ComponentInstance avm_componentinstance) {
        this.avm_componentinstance = avm_componentinstance;
    }

}