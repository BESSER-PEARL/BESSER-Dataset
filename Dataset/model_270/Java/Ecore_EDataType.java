





import java.util.List;
import java.util.ArrayList;

public class Ecore_EDataType extends EClassifier {

    private boolean serializable;





    private Ecore_EAttribute ecore_eattribute;


    public Ecore_EDataType(
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

    public Ecore_EAttribute getEcore_eattribute() {
        return ecore_eattribute;
    }

    public void setEcore_eattribute(Ecore_EAttribute ecore_eattribute) {
        this.ecore_eattribute = ecore_eattribute;
    }

}