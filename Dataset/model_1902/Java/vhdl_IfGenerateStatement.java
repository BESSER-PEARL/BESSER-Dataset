





import java.util.List;
import java.util.ArrayList;

public class vhdl_IfGenerateStatement extends ArchitectureStatement {






    private List<vhdl_ArchitectureStatement> vhdl_architecturestatements;




    private List<vhdl_BlockDeclarativeItem> vhdl_blockdeclarativeitems;




    private vhdl_Expression vhdl_expression;


    public vhdl_IfGenerateStatement(
    ) {
        super(
        );
        this.vhdl_architecturestatements = new ArrayList<>();
        this.vhdl_blockdeclarativeitems = new ArrayList<>();
    }

    public vhdl_IfGenerateStatement(
        ArrayList<vhdl_ArchitectureStatement> vhdl_architecturestatements,        ArrayList<vhdl_BlockDeclarativeItem> vhdl_blockdeclarativeitems    ) {
        this.vhdl_architecturestatements = vhdl_architecturestatements;
        this.vhdl_blockdeclarativeitems = vhdl_blockdeclarativeitems;
    }


    public List<vhdl_ArchitectureStatement> getVhdl_architecturestatements() {
        return vhdl_architecturestatements;
    }

    public void addVhdl_architecturestatement(Vhdl_architecturestatement vhdl_architecturestatement) {
        this.vhdl_architecturestatements.add(vhdl_architecturestatement);
    }
    public List<vhdl_BlockDeclarativeItem> getVhdl_blockdeclarativeitems() {
        return vhdl_blockdeclarativeitems;
    }

    public void addVhdl_blockdeclarativeitem(Vhdl_blockdeclarativeitem vhdl_blockdeclarativeitem) {
        this.vhdl_blockdeclarativeitems.add(vhdl_blockdeclarativeitem);
    }
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}