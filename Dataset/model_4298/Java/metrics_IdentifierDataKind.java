





import java.util.List;
import java.util.ArrayList;

public class metrics_IdentifierDataKind extends DataKind {

    private String objectAttribute;
    private String objectName;



    public metrics_IdentifierDataKind(
        String objectAttribute,        String objectName    ) {
        super(
        );
        this.objectAttribute = objectAttribute;
        this.objectName = objectName;
    }


    public String getObjectattribute() {
        return objectAttribute;
    }

    public void setObjectattribute(String objectAttribute) {
        this.objectAttribute = objectAttribute;
    }
    public String getObjectname() {
        return objectName;
    }

    public void setObjectname(String objectName) {
        this.objectName = objectName;
    }


}