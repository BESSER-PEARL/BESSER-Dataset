





import java.util.List;
import java.util.ArrayList;

public class cmof_NamedElement extends Element {

    private String qualifiedName;
    private String visibility;
    private String name;





    private cmof_Classifier cmof_classifier;




    private cmof_Namespace cmof_namespace;




    private cmof_Namespace cmof_namespace;




    private cmof_Namespace cmof_namespace;


    public cmof_NamedElement(
        String qualifiedName,        String visibility,        String name    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.visibility = visibility;
        this.name = name;
    }


    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cmof_Classifier getCmof_classifier() {
        return cmof_classifier;
    }

    public void setCmof_classifier(cmof_Classifier cmof_classifier) {
        this.cmof_classifier = cmof_classifier;
    }
    public cmof_Namespace getCmof_namespace() {
        return cmof_namespace;
    }

    public void setCmof_namespace(cmof_Namespace cmof_namespace) {
        this.cmof_namespace = cmof_namespace;
    }
    public cmof_Namespace getCmof_namespace() {
        return cmof_namespace;
    }

    public void setCmof_namespace(cmof_Namespace cmof_namespace) {
        this.cmof_namespace = cmof_namespace;
    }
    public cmof_Namespace getCmof_namespace() {
        return cmof_namespace;
    }

    public void setCmof_namespace(cmof_Namespace cmof_namespace) {
        this.cmof_namespace = cmof_namespace;
    }

}