





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ApplyFunctionAction extends Action {






    private List<UML2WithID_InputPin> uml2withid_inputpins;




    private List<UML2WithID_OutputPin> uml2withid_outputpins;




    private UML2WithID_PrimitiveFunction uml2withid_primitivefunction;


    public UML2WithID_ApplyFunctionAction(
    ) {
        super(
        );
        this.uml2withid_inputpins = new ArrayList<>();
        this.uml2withid_outputpins = new ArrayList<>();
    }

    public UML2WithID_ApplyFunctionAction(
        ArrayList<UML2WithID_InputPin> uml2withid_inputpins,        ArrayList<UML2WithID_OutputPin> uml2withid_outputpins    ) {
        this.uml2withid_inputpins = uml2withid_inputpins;
        this.uml2withid_outputpins = uml2withid_outputpins;
    }


    public List<UML2WithID_InputPin> getUml2withid_inputpins() {
        return uml2withid_inputpins;
    }

    public void addUml2withid_inputpin(Uml2withid_inputpin uml2withid_inputpin) {
        this.uml2withid_inputpins.add(uml2withid_inputpin);
    }
    public List<UML2WithID_OutputPin> getUml2withid_outputpins() {
        return uml2withid_outputpins;
    }

    public void addUml2withid_outputpin(Uml2withid_outputpin uml2withid_outputpin) {
        this.uml2withid_outputpins.add(uml2withid_outputpin);
    }
    public UML2WithID_PrimitiveFunction getUml2withid_primitivefunction() {
        return uml2withid_primitivefunction;
    }

    public void setUml2withid_primitivefunction(UML2WithID_PrimitiveFunction uml2withid_primitivefunction) {
        this.uml2withid_primitivefunction = uml2withid_primitivefunction;
    }

}