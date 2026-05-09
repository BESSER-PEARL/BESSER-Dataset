





import java.util.List;
import java.util.ArrayList;

public class javaless_EDataType extends EClassifier {

    private boolean serializable;



    public javaless_EDataType(
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