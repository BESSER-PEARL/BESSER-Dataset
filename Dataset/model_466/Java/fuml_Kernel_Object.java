





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_Object extends ExtensionalValue {






    private List<Kernel_Class> kernel_classs;


    public fuml_Kernel_Object(
    ) {
        super(
        );
        this.kernel_classs = new ArrayList<>();
    }

    public fuml_Kernel_Object(
        ArrayList<Kernel_Class> kernel_classs    ) {
        this.kernel_classs = kernel_classs;
    }


    public List<Kernel_Class> getKernel_classs() {
        return kernel_classs;
    }

    public void addKernel_class(Kernel_class kernel_class) {
        this.kernel_classs.add(kernel_class);
    }

}