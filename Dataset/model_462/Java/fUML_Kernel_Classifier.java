





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Classifier extends Kernel_Type, Kernel_Namespace {

    private boolean finalSpecialization;
    private boolean abstract;



    public fUML_Kernel_Classifier(
        boolean finalSpecialization,        boolean abstract    ) {
        super(
        );
        this.finalSpecialization = finalSpecialization;
        this.abstract = abstract;
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


}