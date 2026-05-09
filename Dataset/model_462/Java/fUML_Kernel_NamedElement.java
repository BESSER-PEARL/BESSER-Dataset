





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_NamedElement extends Element {

    private String visibility;
    private String qualifiedName;
    private String name;





    private Kernel_Namespace kernel_namespace;


    public fUML_Kernel_NamedElement(
        String visibility,        String qualifiedName,        String name    ) {
        super(
        );
        this.visibility = visibility;
        this.qualifiedName = qualifiedName;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Kernel_Namespace getKernel_namespace() {
        return kernel_namespace;
    }

    public void setKernel_namespace(Kernel_Namespace kernel_namespace) {
        this.kernel_namespace = kernel_namespace;
    }

}