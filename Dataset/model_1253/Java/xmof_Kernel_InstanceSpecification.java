





import java.util.List;
import java.util.ArrayList;

public class xmof_Kernel_InstanceSpecification extends ENamedElement {






    private List<Kernel_xmof_EClassifier> kernel_xmof_eclassifiers;


    public xmof_Kernel_InstanceSpecification(
    ) {
        super(
        );
        this.kernel_xmof_eclassifiers = new ArrayList<>();
    }

    public xmof_Kernel_InstanceSpecification(
        ArrayList<Kernel_xmof_EClassifier> kernel_xmof_eclassifiers    ) {
        this.kernel_xmof_eclassifiers = kernel_xmof_eclassifiers;
    }


    public List<Kernel_xmof_EClassifier> getKernel_xmof_eclassifiers() {
        return kernel_xmof_eclassifiers;
    }

    public void addKernel_xmof_eclassifier(Kernel_xmof_eclassifier kernel_xmof_eclassifier) {
        this.kernel_xmof_eclassifiers.add(kernel_xmof_eclassifier);
    }

}