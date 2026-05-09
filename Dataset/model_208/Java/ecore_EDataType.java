





import java.util.List;
import java.util.ArrayList;

public class ecore_EDataType extends EClassifier {

    private String serializable;



    public ecore_EDataType(
        String serializable    ) {
        super(
        );
        this.serializable = serializable;
    }


    public String getSerializable() {
        return serializable;
    }

    public void setSerializable(String serializable) {
        this.serializable = serializable;
    }


}