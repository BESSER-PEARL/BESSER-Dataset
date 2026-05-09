





import java.util.List;
import java.util.ArrayList;

public class RefUML_NamedElement extends Element {

    private String qualifiedName;
    private String name;
    private String visibility;



    public RefUML_NamedElement(
        String qualifiedName,        String name,        String visibility    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.name = name;
        this.visibility = visibility;
    }


    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
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


}