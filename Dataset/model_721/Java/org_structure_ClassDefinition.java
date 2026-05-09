





import java.util.List;
import java.util.ArrayList;

public class org_structure_ClassDefinition extends GenericTypeDefinition {

    private String isFinal;
    private String isAbstract;
    private String isSingleton;



    public org_structure_ClassDefinition(
        String isFinal,        String isAbstract,        String isSingleton    ) {
        super(
        );
        this.isFinal = isFinal;
        this.isAbstract = isAbstract;
        this.isSingleton = isSingleton;
    }


    public String getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(String isFinal) {
        this.isFinal = isFinal;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getIssingleton() {
        return isSingleton;
    }

    public void setIssingleton(String isSingleton) {
        this.isSingleton = isSingleton;
    }


}