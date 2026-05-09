





import java.util.List;
import java.util.ArrayList;

public class ecore_EDataType extends EClassifier {

    private boolean serializable;





    private ecore_EAttribute ecore_eattribute;


    public ecore_EDataType(
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

    public ecore_EAttribute getEcore_eattribute() {
        return ecore_eattribute;
    }

    public void setEcore_eattribute(ecore_EAttribute ecore_eattribute) {
        this.ecore_eattribute = ecore_eattribute;
    }

}