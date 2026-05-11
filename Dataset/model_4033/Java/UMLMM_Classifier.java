





import java.util.List;
import java.util.ArrayList;

public class UMLMM_Classifier extends TemplateableElement, Namespace, Type, RedefinableElement {

    private String isAbstract;



    public UMLMM_Classifier(
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