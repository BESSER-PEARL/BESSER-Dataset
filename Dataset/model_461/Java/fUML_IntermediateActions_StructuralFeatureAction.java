





import java.util.List;
import java.util.ArrayList;

public class fUML_IntermediateActions_StructuralFeatureAction extends Action {






    private Kernel_StructuralFeature kernel_structuralfeature;




    private BasicActions_InputPin basicactions_inputpin;


    public fUML_IntermediateActions_StructuralFeatureAction(
    ) {
        super(
        );
    }



    public Kernel_StructuralFeature getKernel_structuralfeature() {
        return kernel_structuralfeature;
    }

    public void setKernel_structuralfeature(Kernel_StructuralFeature kernel_structuralfeature) {
        this.kernel_structuralfeature = kernel_structuralfeature;
    }
    public BasicActions_InputPin getBasicactions_inputpin() {
        return basicactions_inputpin;
    }

    public void setBasicactions_inputpin(BasicActions_InputPin basicactions_inputpin) {
        this.basicactions_inputpin = basicactions_inputpin;
    }

}