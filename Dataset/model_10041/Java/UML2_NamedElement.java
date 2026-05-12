





import java.util.List;
import java.util.ArrayList;

public class UML2_NamedElement extends TemplateableElement {

    private String name;
    private String visibility;
    private String qualifiedName;



    public UML2_NamedElement(
        String name,        String visibility,        String qualifiedName    ) {
        super(
        );
        this.name = name;
        this.visibility = visibility;
        this.qualifiedName = qualifiedName;
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


}