





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_NamedElement extends TemplateableElement {

    private String name;
    private String visibility;
    private String qualifiedName;





    private UML2WithID_Classifier uml2withid_classifier;




    private UML2WithID_Dependency uml2withid_dependency;




    private UML2WithID_Dependency uml2withid_dependency;




    private List<UML2WithID_Dependency> uml2withid_dependencys;


    public UML2WithID_NamedElement(
        String name,        String visibility,        String qualifiedName    ) {
        super(
        );
        this.name = name;
        this.visibility = visibility;
        this.qualifiedName = qualifiedName;
        this.uml2withid_dependencys = new ArrayList<>();
    }

    public UML2WithID_NamedElement(
        String name,        String visibility,        String qualifiedName        ArrayList<UML2WithID_Dependency> uml2withid_dependencys    ) {
        this.name = name;
        this.visibility = visibility;
        this.qualifiedName = qualifiedName;
        this.uml2withid_dependencys = uml2withid_dependencys;
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
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }

    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public UML2WithID_Dependency getUml2withid_dependency() {
        return uml2withid_dependency;
    }

    public void setUml2withid_dependency(UML2WithID_Dependency uml2withid_dependency) {
        this.uml2withid_dependency = uml2withid_dependency;
    }
    public UML2WithID_Dependency getUml2withid_dependency() {
        return uml2withid_dependency;
    }

    public void setUml2withid_dependency(UML2WithID_Dependency uml2withid_dependency) {
        this.uml2withid_dependency = uml2withid_dependency;
    }
    public List<UML2WithID_Dependency> getUml2withid_dependencys() {
        return uml2withid_dependencys;
    }

    public void addUml2withid_dependency(Uml2withid_dependency uml2withid_dependency) {
        this.uml2withid_dependencys.add(uml2withid_dependency);
    }

}