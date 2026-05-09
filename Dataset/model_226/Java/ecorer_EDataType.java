





import java.util.List;
import java.util.ArrayList;

public class ecorer_EDataType extends EClassifier {

    private boolean serializable;





    private ecorer_EAttribute ecorer_eattribute;


    public ecorer_EDataType(
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

    public ecorer_EAttribute getEcorer_eattribute() {
        return ecorer_eattribute;
    }

    public void setEcorer_eattribute(ecorer_EAttribute ecorer_eattribute) {
        this.ecorer_eattribute = ecorer_eattribute;
    }

}