





import java.util.List;
import java.util.ArrayList;

public class vhdl_LoopStatement extends SequentialStatement {






    private List<vhdl_SequentialStatement> vhdl_sequentialstatements;




    private vhdl_LoopVariable vhdl_loopvariable;




    private vhdl_Expression vhdl_expression;


    public vhdl_LoopStatement(
    ) {
        super(
        );
        this.vhdl_sequentialstatements = new ArrayList<>();
    }

    public vhdl_LoopStatement(
        ArrayList<vhdl_SequentialStatement> vhdl_sequentialstatements    ) {
        this.vhdl_sequentialstatements = vhdl_sequentialstatements;
    }


    public List<vhdl_SequentialStatement> getVhdl_sequentialstatements() {
        return vhdl_sequentialstatements;
    }

    public void addVhdl_sequentialstatement(Vhdl_sequentialstatement vhdl_sequentialstatement) {
        this.vhdl_sequentialstatements.add(vhdl_sequentialstatement);
    }
    public vhdl_LoopVariable getVhdl_loopvariable() {
        return vhdl_loopvariable;
    }

    public void setVhdl_loopvariable(vhdl_LoopVariable vhdl_loopvariable) {
        this.vhdl_loopvariable = vhdl_loopvariable;
    }
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}