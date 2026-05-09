





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_NamedElement extends Element {

    private String visibility;
    private String name;
    private String qualifiedName;



    public fUML_Kernel_NamedElement(
        String visibility,        String name,        String qualifiedName    ) {
        super(
        );
        this.visibility = visibility;
        this.name = name;
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
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }


}