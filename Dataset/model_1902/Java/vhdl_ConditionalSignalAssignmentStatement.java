





import java.util.List;
import java.util.ArrayList;

public class vhdl_ConditionalSignalAssignmentStatement extends ArchitectureStatement {

    private boolean postponed;
    private boolean guarded;





    private vhdl_Expression vhdl_expression;




    private List<vhdl_Expression> vhdl_expressions;


    public vhdl_ConditionalSignalAssignmentStatement(
        boolean postponed,        boolean guarded    ) {
        super(
        );
        this.postponed = postponed;
        this.guarded = guarded;
        this.vhdl_expressions = new ArrayList<>();
    }

    public vhdl_ConditionalSignalAssignmentStatement(
        boolean postponed,        boolean guarded        ArrayList<vhdl_Expression> vhdl_expressions    ) {
        this.postponed = postponed;
        this.guarded = guarded;
        this.vhdl_expressions = vhdl_expressions;
    }

    public boolean getPostponed() {
        return postponed;
    }

    public void setPostponed(boolean postponed) {
        this.postponed = postponed;
    }
    public boolean getGuarded() {
        return guarded;
    }

    public void setGuarded(boolean guarded) {
        this.guarded = guarded;
    }

    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }
    public List<vhdl_Expression> getVhdl_expressions() {
        return vhdl_expressions;
    }

    public void addVhdl_expression(Vhdl_expression vhdl_expression) {
        this.vhdl_expressions.add(vhdl_expression);
    }

}