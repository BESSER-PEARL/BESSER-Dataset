





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_EnumerationValue extends Value {






    private Kernel_Enumeration kernel_enumeration;




    private Kernel_EnumerationLiteral kernel_enumerationliteral;


    public fUML_Kernel_EnumerationValue(
    ) {
        super(
        );
    }



    public Kernel_Enumeration getKernel_enumeration() {
        return kernel_enumeration;
    }

    public void setKernel_enumeration(Kernel_Enumeration kernel_enumeration) {
        this.kernel_enumeration = kernel_enumeration;
    }
    public Kernel_EnumerationLiteral getKernel_enumerationliteral() {
        return kernel_enumerationliteral;
    }

    public void setKernel_enumerationliteral(Kernel_EnumerationLiteral kernel_enumerationliteral) {
        this.kernel_enumerationliteral = kernel_enumerationliteral;
    }

}