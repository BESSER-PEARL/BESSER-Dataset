





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Class extends BehavioredClassifier {

    private boolean active;





    private List<Kernel_Class> kernel_classs;




    private List<Kernel_Operation> kernel_operations;


    public fUML_Kernel_Class(
        boolean active    ) {
        super(
        );
        this.active = active;
        this.kernel_classs = new ArrayList<>();
        this.kernel_operations = new ArrayList<>();
    }

    public fUML_Kernel_Class(
        boolean active        ArrayList<Kernel_Class> kernel_classs,        ArrayList<Kernel_Operation> kernel_operations    ) {
        this.active = active;
        this.kernel_classs = kernel_classs;
        this.kernel_operations = kernel_operations;
    }

    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public List<Kernel_Class> getKernel_classs() {
        return kernel_classs;
    }

    public void addKernel_class(Kernel_class kernel_class) {
        this.kernel_classs.add(kernel_class);
    }
    public List<Kernel_Operation> getKernel_operations() {
        return kernel_operations;
    }

    public void addKernel_operation(Kernel_operation kernel_operation) {
        this.kernel_operations.add(kernel_operation);
    }

}