





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Slot extends Element {






    private List<Kernel_ValueSpecification> kernel_valuespecifications;


    public fUML_Kernel_Slot(
    ) {
        super(
        );
        this.kernel_valuespecifications = new ArrayList<>();
    }

    public fUML_Kernel_Slot(
        ArrayList<Kernel_ValueSpecification> kernel_valuespecifications    ) {
        this.kernel_valuespecifications = kernel_valuespecifications;
    }


    public List<Kernel_ValueSpecification> getKernel_valuespecifications() {
        return kernel_valuespecifications;
    }

    public void addKernel_valuespecification(Kernel_valuespecification kernel_valuespecification) {
        this.kernel_valuespecifications.add(kernel_valuespecification);
    }

}