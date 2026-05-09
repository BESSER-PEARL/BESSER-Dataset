





import java.util.List;
import java.util.ArrayList;

public class UML2_NamedElement extends TemplateableElement {

    private String name;
    private String visibility;





    private UML2_Classifier uml2_classifier;




    private UML2_Namespace uml2_namespace;


    public UML2_NamedElement(
        String name,        String visibility    ) {
        super(
        );
        this.name = name;
        this.visibility = visibility;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public UML2_Namespace getUml2_namespace() {
        return uml2_namespace;
    }

    public void setUml2_namespace(UML2_Namespace uml2_namespace) {
        this.uml2_namespace = uml2_namespace;
    }

}