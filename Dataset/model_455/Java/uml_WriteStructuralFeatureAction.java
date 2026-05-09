





import java.util.List;
import java.util.ArrayList;

public class uml_WriteStructuralFeatureAction extends StructuralFeatureAction {






    private uml_OutputPin uml_outputpin;




    private uml_InputPin uml_inputpin;


    public uml_WriteStructuralFeatureAction(
    ) {
        super(
        );
    }



    public uml_OutputPin getUml_outputpin() {
        return uml_outputpin;
    }

    public void setUml_outputpin(uml_OutputPin uml_outputpin) {
        this.uml_outputpin = uml_outputpin;
    }
    public uml_InputPin getUml_inputpin() {
        return uml_inputpin;
    }

    public void setUml_inputpin(uml_InputPin uml_inputpin) {
        this.uml_inputpin = uml_inputpin;
    }

}