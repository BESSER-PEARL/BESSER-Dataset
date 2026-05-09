





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Enumeration extends DataType {






    private List<Kernel_EnumerationLiteral> kernel_enumerationliterals;


    public fUML_Kernel_Enumeration(
    ) {
        super(
        );
        this.kernel_enumerationliterals = new ArrayList<>();
    }

    public fUML_Kernel_Enumeration(
        ArrayList<Kernel_EnumerationLiteral> kernel_enumerationliterals    ) {
        this.kernel_enumerationliterals = kernel_enumerationliterals;
    }


    public List<Kernel_EnumerationLiteral> getKernel_enumerationliterals() {
        return kernel_enumerationliterals;
    }

    public void addKernel_enumerationliteral(Kernel_enumerationliteral kernel_enumerationliteral) {
        this.kernel_enumerationliterals.add(kernel_enumerationliteral);
    }

}