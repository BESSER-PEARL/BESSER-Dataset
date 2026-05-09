





import java.util.List;
import java.util.ArrayList;

public class uml_LoopNode extends StructuredActivityNode {

    private String isTestedFirst;





    private List<uml_OutputPin> uml_outputpins;




    private List<uml_ExecutableNode> uml_executablenodes;




    private List<uml_InputPin> uml_inputpins;




    private List<uml_ExecutableNode> uml_executablenodes;




    private uml_OutputPin uml_outputpin;




    private List<uml_OutputPin> uml_outputpins;




    private List<uml_OutputPin> uml_outputpins;




    private List<uml_ExecutableNode> uml_executablenodes;


    public uml_LoopNode(
        String isTestedFirst    ) {
        super(
        );
        this.isTestedFirst = isTestedFirst;
        this.uml_outputpins = new ArrayList<>();
        this.uml_executablenodes = new ArrayList<>();
        this.uml_inputpins = new ArrayList<>();
        this.uml_executablenodes = new ArrayList<>();
        this.uml_outputpins = new ArrayList<>();
        this.uml_outputpins = new ArrayList<>();
        this.uml_executablenodes = new ArrayList<>();
    }

    public uml_LoopNode(
        String isTestedFirst        ArrayList<uml_OutputPin> uml_outputpins,        ArrayList<uml_ExecutableNode> uml_executablenodes,        ArrayList<uml_InputPin> uml_inputpins,        ArrayList<uml_ExecutableNode> uml_executablenodes,        ArrayList<uml_OutputPin> uml_outputpins,        ArrayList<uml_OutputPin> uml_outputpins,        ArrayList<uml_ExecutableNode> uml_executablenodes    ) {
        this.isTestedFirst = isTestedFirst;
        this.uml_outputpins = uml_outputpins;
        this.uml_executablenodes = uml_executablenodes;
        this.uml_inputpins = uml_inputpins;
        this.uml_executablenodes = uml_executablenodes;
        this.uml_outputpins = uml_outputpins;
        this.uml_outputpins = uml_outputpins;
        this.uml_executablenodes = uml_executablenodes;
    }

    public String getIstestedfirst() {
        return isTestedFirst;
    }

    public void setIstestedfirst(String isTestedFirst) {
        this.isTestedFirst = isTestedFirst;
    }

    public List<uml_OutputPin> getUml_outputpins() {
        return uml_outputpins;
    }

    public void addUml_outputpin(Uml_outputpin uml_outputpin) {
        this.uml_outputpins.add(uml_outputpin);
    }
    public List<uml_ExecutableNode> getUml_executablenodes() {
        return uml_executablenodes;
    }

    public void addUml_executablenode(Uml_executablenode uml_executablenode) {
        this.uml_executablenodes.add(uml_executablenode);
    }
    public List<uml_InputPin> getUml_inputpins() {
        return uml_inputpins;
    }

    public void addUml_inputpin(Uml_inputpin uml_inputpin) {
        this.uml_inputpins.add(uml_inputpin);
    }
    public List<uml_ExecutableNode> getUml_executablenodes() {
        return uml_executablenodes;
    }

    public void addUml_executablenode(Uml_executablenode uml_executablenode) {
        this.uml_executablenodes.add(uml_executablenode);
    }
    public uml_OutputPin getUml_outputpin() {
        return uml_outputpin;
    }

    public void setUml_outputpin(uml_OutputPin uml_outputpin) {
        this.uml_outputpin = uml_outputpin;
    }
    public List<uml_OutputPin> getUml_outputpins() {
        return uml_outputpins;
    }

    public void addUml_outputpin(Uml_outputpin uml_outputpin) {
        this.uml_outputpins.add(uml_outputpin);
    }
    public List<uml_OutputPin> getUml_outputpins() {
        return uml_outputpins;
    }

    public void addUml_outputpin(Uml_outputpin uml_outputpin) {
        this.uml_outputpins.add(uml_outputpin);
    }
    public List<uml_ExecutableNode> getUml_executablenodes() {
        return uml_executablenodes;
    }

    public void addUml_executablenode(Uml_executablenode uml_executablenode) {
        this.uml_executablenodes.add(uml_executablenode);
    }

}