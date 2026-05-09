





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_Classifier extends Kernel_Type, Kernel_Namespace {

    private boolean abstract;
    private boolean finalSpecialization;





    private List<Kernel_Property> kernel_propertys;


    public fuml_Kernel_Classifier(
        boolean abstract,        boolean finalSpecialization    ) {
        super(
        );
        this.abstract = abstract;
        this.finalSpecialization = finalSpecialization;
        this.kernel_propertys = new ArrayList<>();
    }

    public fuml_Kernel_Classifier(
        boolean abstract,        boolean finalSpecialization        ArrayList<Kernel_Property> kernel_propertys    ) {
        this.abstract = abstract;
        this.finalSpecialization = finalSpecialization;
        this.kernel_propertys = kernel_propertys;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getFinalspecialization() {
        return finalSpecialization;
    }

    public void setFinalspecialization(boolean finalSpecialization) {
        this.finalSpecialization = finalSpecialization;
    }

    public List<Kernel_Property> getKernel_propertys() {
        return kernel_propertys;
    }

    public void addKernel_property(Kernel_property kernel_property) {
        this.kernel_propertys.add(kernel_property);
    }

}