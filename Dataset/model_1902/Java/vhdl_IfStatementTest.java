





import java.util.List;
import java.util.ArrayList;

public class vhdl_IfStatementTest  {






    private List<vhdl_SequentialStatement> vhdl_sequentialstatements;




    private vhdl_Expression vhdl_expression;




    private vhdl_IfStatement vhdl_ifstatement;


    public vhdl_IfStatementTest(
    ) {
        this.vhdl_sequentialstatements = new ArrayList<>();
    }

    public vhdl_IfStatementTest(
        ArrayList<vhdl_SequentialStatement> vhdl_sequentialstatements    ) {
        this.vhdl_sequentialstatements = vhdl_sequentialstatements;
    }


    public List<vhdl_SequentialStatement> getVhdl_sequentialstatements() {
        return vhdl_sequentialstatements;
    }

    public void addVhdl_sequentialstatement(Vhdl_sequentialstatement vhdl_sequentialstatement) {
        this.vhdl_sequentialstatements.add(vhdl_sequentialstatement);
    }
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }
    public vhdl_IfStatement getVhdl_ifstatement() {
        return vhdl_ifstatement;
    }

    public void setVhdl_ifstatement(vhdl_IfStatement vhdl_ifstatement) {
        this.vhdl_ifstatement = vhdl_ifstatement;
    }

}