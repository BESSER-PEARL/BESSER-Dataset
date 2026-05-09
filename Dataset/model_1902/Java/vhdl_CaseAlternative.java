





import java.util.List;
import java.util.ArrayList;

public class vhdl_CaseAlternative  {






    private vhdl_Expression vhdl_expression;




    private vhdl_CaseStatement vhdl_casestatement;




    private List<vhdl_SequentialStatement> vhdl_sequentialstatements;


    public vhdl_CaseAlternative(
    ) {
        this.vhdl_sequentialstatements = new ArrayList<>();
    }

    public vhdl_CaseAlternative(
        ArrayList<vhdl_SequentialStatement> vhdl_sequentialstatements    ) {
        this.vhdl_sequentialstatements = vhdl_sequentialstatements;
    }


    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }
    public vhdl_CaseStatement getVhdl_casestatement() {
        return vhdl_casestatement;
    }

    public void setVhdl_casestatement(vhdl_CaseStatement vhdl_casestatement) {
        this.vhdl_casestatement = vhdl_casestatement;
    }
    public List<vhdl_SequentialStatement> getVhdl_sequentialstatements() {
        return vhdl_sequentialstatements;
    }

    public void addVhdl_sequentialstatement(Vhdl_sequentialstatement vhdl_sequentialstatement) {
        this.vhdl_sequentialstatements.add(vhdl_sequentialstatement);
    }

}