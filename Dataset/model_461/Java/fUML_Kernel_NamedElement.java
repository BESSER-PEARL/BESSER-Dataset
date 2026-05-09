





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_NamedElement extends Element {

    private String qualifiedName;
    private String visibility;
    private String name;



    public fUML_Kernel_NamedElement(
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


}