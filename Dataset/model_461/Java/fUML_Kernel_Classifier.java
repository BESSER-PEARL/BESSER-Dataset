





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Classifier extends Kernel_Type, Kernel_Namespace {

    private boolean finalSpecialization;
    private boolean abstract;





    private List<Kernel_Property> kernel_propertys;


    public fUML_Kernel_Classifier(
        boolean finalSpecialization,        boolean abstract    ) {
        super(
        );
        this.finalSpecialization = finalSpecialization;
        this.abstract = abstract;
        this.kernel_propertys = new ArrayList<>();
    }

    public fUML_Kernel_Classifier(
        boolean finalSpecialization,        boolean abstract        ArrayList<Kernel_Property> kernel_propertys    ) {
        this.finalSpecialization = finalSpecialization;
        this.abstract = abstract;
        this.kernel_propertys = kernel_propertys;
    }

    public boolean getFinalspecialization() {
        return finalSpecialization;
    }

    public void setFinalspecialization(boolean finalSpecialization) {
        this.finalSpecialization = finalSpecialization;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<Kernel_Property> getKernel_propertys() {
        return kernel_propertys;
    }

    public void addKernel_property(Kernel_property kernel_property) {
        this.kernel_propertys.add(kernel_property);
    }

}