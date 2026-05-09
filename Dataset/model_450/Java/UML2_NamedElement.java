





import java.util.List;
import java.util.ArrayList;

public class UML2_NamedElement extends TemplateableElement {

    private String visibility;
    private String name;
    private String qualifiedName;





    private UML2_Namespace uml2_namespace;




    private UML2_Duration uml2_duration;




    private List<UML2_Dependency> uml2_dependencys;




    private UML2_TimeExpression uml2_timeexpression;




    private UML2_Message uml2_message;




    private UML2_Dependency uml2_dependency;




    private UML2_Dependency uml2_dependency;




    private UML2_Classifier uml2_classifier;


    public UML2_NamedElement(
        String visibility,        String name,        String qualifiedName    ) {
        super(
        );
        this.visibility = visibility;
        this.name = name;
        this.qualifiedName = qualifiedName;
        this.uml2_dependencys = new ArrayList<>();
    }

    public UML2_NamedElement(
        String visibility,        String name,        String qualifiedName        ArrayList<UML2_Dependency> uml2_dependencys    ) {
        this.visibility = visibility;
        this.name = name;
        this.qualifiedName = qualifiedName;
        this.uml2_dependencys = uml2_dependencys;
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
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }

    public UML2_Namespace getUml2_namespace() {
        return uml2_namespace;
    }

    public void setUml2_namespace(UML2_Namespace uml2_namespace) {
        this.uml2_namespace = uml2_namespace;
    }
    public UML2_Duration getUml2_duration() {
        return uml2_duration;
    }

    public void setUml2_duration(UML2_Duration uml2_duration) {
        this.uml2_duration = uml2_duration;
    }
    public List<UML2_Dependency> getUml2_dependencys() {
        return uml2_dependencys;
    }

    public void addUml2_dependency(Uml2_dependency uml2_dependency) {
        this.uml2_dependencys.add(uml2_dependency);
    }
    public UML2_TimeExpression getUml2_timeexpression() {
        return uml2_timeexpression;
    }

    public void setUml2_timeexpression(UML2_TimeExpression uml2_timeexpression) {
        this.uml2_timeexpression = uml2_timeexpression;
    }
    public UML2_Message getUml2_message() {
        return uml2_message;
    }

    public void setUml2_message(UML2_Message uml2_message) {
        this.uml2_message = uml2_message;
    }
    public UML2_Dependency getUml2_dependency() {
        return uml2_dependency;
    }

    public void setUml2_dependency(UML2_Dependency uml2_dependency) {
        this.uml2_dependency = uml2_dependency;
    }
    public UML2_Dependency getUml2_dependency() {
        return uml2_dependency;
    }

    public void setUml2_dependency(UML2_Dependency uml2_dependency) {
        this.uml2_dependency = uml2_dependency;
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }

}