





import java.util.List;
import java.util.ArrayList;

public class uml_Classifier extends Type, RedefinableElement, Namespace, TemplateableElement {

    private String isAbstract;



    public uml_Classifier(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }


}