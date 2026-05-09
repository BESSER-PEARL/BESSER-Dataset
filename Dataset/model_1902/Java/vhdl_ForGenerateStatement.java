





import java.util.List;
import java.util.ArrayList;

public class vhdl_ForGenerateStatement extends ArchitectureStatement {






    private vhdl_LoopVariable vhdl_loopvariable;




    private vhdl_Expression vhdl_expression;




    private List<vhdl_BlockDeclarativeItem> vhdl_blockdeclarativeitems;




    private List<vhdl_ArchitectureStatement> vhdl_architecturestatements;


    public vhdl_ForGenerateStatement(
    ) {
        super(
        );
        this.vhdl_blockdeclarativeitems = new ArrayList<>();
        this.vhdl_architecturestatements = new ArrayList<>();
    }

    public vhdl_ForGenerateStatement(
        ArrayList<vhdl_BlockDeclarativeItem> vhdl_blockdeclarativeitems,        ArrayList<vhdl_ArchitectureStatement> vhdl_architecturestatements    ) {
        this.vhdl_blockdeclarativeitems = vhdl_blockdeclarativeitems;
        this.vhdl_architecturestatements = vhdl_architecturestatements;
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
    public List<vhdl_BlockDeclarativeItem> getVhdl_blockdeclarativeitems() {
        return vhdl_blockdeclarativeitems;
    }

    public void addVhdl_blockdeclarativeitem(Vhdl_blockdeclarativeitem vhdl_blockdeclarativeitem) {
        this.vhdl_blockdeclarativeitems.add(vhdl_blockdeclarativeitem);
    }
    public List<vhdl_ArchitectureStatement> getVhdl_architecturestatements() {
        return vhdl_architecturestatements;
    }

    public void addVhdl_architecturestatement(Vhdl_architecturestatement vhdl_architecturestatement) {
        this.vhdl_architecturestatements.add(vhdl_architecturestatement);
    }

}