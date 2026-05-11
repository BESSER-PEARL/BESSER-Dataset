





import java.util.List;
import java.util.ArrayList;

public class llp_Block  {






    private llp_RepetitionInstruction llp_repetitioninstruction;




    private llp_LowLevelProgram llp_lowlevelprogram;




    private llp_Task llp_task;




    private List<llp_DataAccessPattern> llp_dataaccesspatterns;




    private llp_ParenthesisInstruction llp_parenthesisinstruction;




    private llp_ControlFlowBranchingInstruction llp_controlflowbranchinginstruction;




    private llp_ControlFlowBranchingInstruction llp_controlflowbranchinginstruction;


    public llp_Block(
    ) {
        this.llp_dataaccesspatterns = new ArrayList<>();
    }

    public llp_Block(
        ArrayList<llp_DataAccessPattern> llp_dataaccesspatterns    ) {
        this.llp_dataaccesspatterns = llp_dataaccesspatterns;
    }


    public llp_RepetitionInstruction getLlp_repetitioninstruction() {
        return llp_repetitioninstruction;
    }

    public void setLlp_repetitioninstruction(llp_RepetitionInstruction llp_repetitioninstruction) {
        this.llp_repetitioninstruction = llp_repetitioninstruction;
    }
    public llp_LowLevelProgram getLlp_lowlevelprogram() {
        return llp_lowlevelprogram;
    }

    public void setLlp_lowlevelprogram(llp_LowLevelProgram llp_lowlevelprogram) {
        this.llp_lowlevelprogram = llp_lowlevelprogram;
    }
    public llp_Task getLlp_task() {
        return llp_task;
    }

    public void setLlp_task(llp_Task llp_task) {
        this.llp_task = llp_task;
    }
    public List<llp_DataAccessPattern> getLlp_dataaccesspatterns() {
        return llp_dataaccesspatterns;
    }

    public void addLlp_dataaccesspattern(Llp_dataaccesspattern llp_dataaccesspattern) {
        this.llp_dataaccesspatterns.add(llp_dataaccesspattern);
    }
    public llp_ParenthesisInstruction getLlp_parenthesisinstruction() {
        return llp_parenthesisinstruction;
    }

    public void setLlp_parenthesisinstruction(llp_ParenthesisInstruction llp_parenthesisinstruction) {
        this.llp_parenthesisinstruction = llp_parenthesisinstruction;
    }
    public llp_ControlFlowBranchingInstruction getLlp_controlflowbranchinginstruction() {
        return llp_controlflowbranchinginstruction;
    }

    public void setLlp_controlflowbranchinginstruction(llp_ControlFlowBranchingInstruction llp_controlflowbranchinginstruction) {
        this.llp_controlflowbranchinginstruction = llp_controlflowbranchinginstruction;
    }
    public llp_ControlFlowBranchingInstruction getLlp_controlflowbranchinginstruction() {
        return llp_controlflowbranchinginstruction;
    }

    public void setLlp_controlflowbranchinginstruction(llp_ControlFlowBranchingInstruction llp_controlflowbranchinginstruction) {
        this.llp_controlflowbranchinginstruction = llp_controlflowbranchinginstruction;
    }

}