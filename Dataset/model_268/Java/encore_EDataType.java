





import java.util.List;
import java.util.ArrayList;

public class encore_EDataType extends EClassifier {

    private boolean serializable;





    private encore_EAttribute encore_eattribute;


    public encore_EDataType(
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

    public encore_EAttribute getEncore_eattribute() {
        return encore_eattribute;
    }

    public void setEncore_eattribute(encore_EAttribute encore_eattribute) {
        this.encore_eattribute = encore_eattribute;
    }

}