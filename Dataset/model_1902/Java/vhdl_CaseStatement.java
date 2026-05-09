





import java.util.List;
import java.util.ArrayList;

public class vhdl_CaseStatement extends SequentialStatement {

    private String label;





    private vhdl_Expression vhdl_expression;


    public vhdl_CaseStatement(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}