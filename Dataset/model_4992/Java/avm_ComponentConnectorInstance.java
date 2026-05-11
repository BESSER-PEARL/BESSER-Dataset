





import java.util.List;
import java.util.ArrayList;

public class avm_ComponentConnectorInstance extends ConnectorCompositionTarget {

    private String IDinComponentModel;



    public avm_ComponentConnectorInstance(
        String IDinComponentModel    ) {
        super(
        );
        this.IDinComponentModel = IDinComponentModel;
    }


    public String getIdincomponentmodel() {
        return IDinComponentModel;
    }

    public void setIdincomponentmodel(String IDinComponentModel) {
        this.IDinComponentModel = IDinComponentModel;
    }


}