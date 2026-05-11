





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EDataType extends EClassifier {

    private boolean serializable;



    public ecoreDiff_EDataType(
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


}