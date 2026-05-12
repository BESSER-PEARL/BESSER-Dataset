





import java.util.List;
import java.util.ArrayList;

public class UML2_ApplyFunctionAction extends Action {






    private UML2_PrimitiveFunction uml2_primitivefunction;




    private List<UML2_OutputPin> uml2_outputpins;




    private List<UML2_InputPin> uml2_inputpins;


    public UML2_ApplyFunctionAction(
    ) {
        super(
        );
        this.uml2_outputpins = new ArrayList<>();
        this.uml2_inputpins = new ArrayList<>();
    }

    public UML2_ApplyFunctionAction(
        ArrayList<UML2_OutputPin> uml2_outputpins,        ArrayList<UML2_InputPin> uml2_inputpins    ) {
        this.uml2_outputpins = uml2_outputpins;
        this.uml2_inputpins = uml2_inputpins;
    }


    public UML2_PrimitiveFunction getUml2_primitivefunction() {
        return uml2_primitivefunction;
    }

    public void setUml2_primitivefunction(UML2_PrimitiveFunction uml2_primitivefunction) {
        this.uml2_primitivefunction = uml2_primitivefunction;
    }
    public List<UML2_OutputPin> getUml2_outputpins() {
        return uml2_outputpins;
    }

    public void addUml2_outputpin(Uml2_outputpin uml2_outputpin) {
        this.uml2_outputpins.add(uml2_outputpin);
    }
    public List<UML2_InputPin> getUml2_inputpins() {
        return uml2_inputpins;
    }

    public void addUml2_inputpin(Uml2_inputpin uml2_inputpin) {
        this.uml2_inputpins.add(uml2_inputpin);
    }

}