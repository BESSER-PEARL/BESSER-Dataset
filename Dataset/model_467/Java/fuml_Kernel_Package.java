





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_Package extends Kernel_Namespace, Kernel_PackageableElement {






    private List<Kernel_Type> kernel_types;


    public fuml_Kernel_Package(
    ) {
        super(
        );
        this.kernel_types = new ArrayList<>();
    }

    public fuml_Kernel_Package(
        ArrayList<Kernel_Type> kernel_types    ) {
        this.kernel_types = kernel_types;
    }


    public List<Kernel_Type> getKernel_types() {
        return kernel_types;
    }

    public void addKernel_type(Kernel_type kernel_type) {
        this.kernel_types.add(kernel_type);
    }

}