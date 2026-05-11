





import java.util.List;
import java.util.ArrayList;

public class systemmodel_DataType extends SMElement {

    private String basetype;





    private systemmodel_SystemModel systemmodel_systemmodel;


    public systemmodel_DataType(
        String basetype    ) {
        super(
        );
        this.basetype = basetype;
    }


    public String getBasetype() {
        return basetype;
    }

    public void setBasetype(String basetype) {
        this.basetype = basetype;
    }

    public systemmodel_SystemModel getSystemmodel_systemmodel() {
        return systemmodel_systemmodel;
    }

    public void setSystemmodel_systemmodel(systemmodel_SystemModel systemmodel_systemmodel) {
        this.systemmodel_systemmodel = systemmodel_systemmodel;
    }

}