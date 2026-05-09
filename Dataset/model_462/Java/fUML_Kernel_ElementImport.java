





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_ElementImport extends Element {

    private String alias;
    private String visibility;





    private Kernel_Namespace kernel_namespace;


    public fUML_Kernel_ElementImport(
        String alias,        String visibility    ) {
        super(
        );
        this.alias = alias;
        this.visibility = visibility;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public Kernel_Namespace getKernel_namespace() {
        return kernel_namespace;
    }

    public void setKernel_namespace(Kernel_Namespace kernel_namespace) {
        this.kernel_namespace = kernel_namespace;
    }

}