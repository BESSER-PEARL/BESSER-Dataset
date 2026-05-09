





import java.util.List;
import java.util.ArrayList;

public class vhdl_WaitStatement extends SequentialStatement {

    private String label;





    private vhdl_Expression vhdl_expression;




    private vhdl_Expression vhdl_expression;




    private vhdl_IdList vhdl_idlist;


    public vhdl_WaitStatement(
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
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }
    public vhdl_IdList getVhdl_idlist() {
        return vhdl_idlist;
    }

    public void setVhdl_idlist(vhdl_IdList vhdl_idlist) {
        this.vhdl_idlist = vhdl_idlist;
    }

}