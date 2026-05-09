





import java.util.List;
import java.util.ArrayList;

public class vhdl_SequentialSignalAssignmentStatement extends SequentialStatement {

    private String label;
    private boolean postponed;
    private boolean guarded;





    private vhdl_Expression vhdl_expression;




    private vhdl_Expression vhdl_expression;


    public vhdl_SequentialSignalAssignmentStatement(
        String label,        boolean postponed,        boolean guarded    ) {
        super(
        );
        this.label = label;
        this.postponed = postponed;
        this.guarded = guarded;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}