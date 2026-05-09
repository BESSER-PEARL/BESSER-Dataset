





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Extension extends Association {

    private String metaClass;
    private String isRequired;



    public UMLModel_Extension(
        String metaClass,        String isRequired    ) {
        super(
        );
        this.metaClass = metaClass;
        this.isRequired = isRequired;
    }


    public String getMetaclass() {
        return metaClass;
    }

    public void setMetaclass(String metaClass) {
        this.metaClass = metaClass;
    }
    public String getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(String isRequired) {
        this.isRequired = isRequired;
    }


}