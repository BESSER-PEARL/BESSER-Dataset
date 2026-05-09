





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_NamedElement extends Element {

    private String name;
    private String qualifiedName;
    private String visibility;



    public fuml_Kernel_NamedElement(
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


}