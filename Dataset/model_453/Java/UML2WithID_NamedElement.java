





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_NamedElement extends TemplateableElement {

    private String name;
    private String qualifiedName;
    private String visibility;





    private UML2WithID_Duration uml2withid_duration;




    private UML2WithID_TimeExpression uml2withid_timeexpression;


    public UML2WithID_NamedElement(
        String name,        String qualifiedName,        String visibility    ) {
        super(
        );
        this.name = name;
        this.qualifiedName = qualifiedName;
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
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public UML2WithID_Duration getUml2withid_duration() {
        return uml2withid_duration;
    }

    public void setUml2withid_duration(UML2WithID_Duration uml2withid_duration) {
        this.uml2withid_duration = uml2withid_duration;
    }
    public UML2WithID_TimeExpression getUml2withid_timeexpression() {
        return uml2withid_timeexpression;
    }

    public void setUml2withid_timeexpression(UML2WithID_TimeExpression uml2withid_timeexpression) {
        this.uml2withid_timeexpression = uml2withid_timeexpression;
    }

}