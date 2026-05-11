





import java.util.List;
import java.util.ArrayList;

public class crom_l1_composed_DataType extends RigidType {

    private boolean serializable;





    private crom_l1_composed_DataType crom_l1_composed_datatype;


    public crom_l1_composed_DataType(
        boolean serializable    ) {
        super(
        );
        this.serializable = serializable;
    }


    public boolean getSerializable() {
        return serializable;
    }

    public void setSerializable(boolean serializable) {
        this.serializable = serializable;
    }

    public crom_l1_composed_DataType getCrom_l1_composed_datatype() {
        return crom_l1_composed_datatype;
    }

    public void setCrom_l1_composed_datatype(crom_l1_composed_DataType crom_l1_composed_datatype) {
        this.crom_l1_composed_datatype = crom_l1_composed_datatype;
    }

}