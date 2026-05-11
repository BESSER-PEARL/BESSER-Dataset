





import java.util.List;
import java.util.ArrayList;

public class Statement  {






    private vhdl_Entity vhdl_entity;




    private vhdl_Architecture vhdl_architecture;




    private vhdl_statement_ProcessStatement vhdl_statement_processstatement;




    private vhdl_statement_IfStatement vhdl_statement_ifstatement;




    private vhdl_statement_BlockStatement vhdl_statement_blockstatement;




    private vhdl_statement_SimultaneousProceduralStatement vhdl_statement_simultaneousproceduralstatement;




    private vhdl_statement_LoopStatement vhdl_statement_loopstatement;




    private vhdl_statement_GenerateStatement vhdl_statement_generatestatement;


    public Statement(
    ) {
    }



    public vhdl_Entity getVhdl_entity() {
        return vhdl_entity;
    }

    public void setVhdl_entity(vhdl_Entity vhdl_entity) {
        this.vhdl_entity = vhdl_entity;
    }
    public vhdl_Architecture getVhdl_architecture() {
        return vhdl_architecture;
    }

    public void setVhdl_architecture(vhdl_Architecture vhdl_architecture) {
        this.vhdl_architecture = vhdl_architecture;
    }
    public vhdl_statement_ProcessStatement getVhdl_statement_processstatement() {
        return vhdl_statement_processstatement;
    }

    public void setVhdl_statement_processstatement(vhdl_statement_ProcessStatement vhdl_statement_processstatement) {
        this.vhdl_statement_processstatement = vhdl_statement_processstatement;
    }
    public vhdl_statement_IfStatement getVhdl_statement_ifstatement() {
        return vhdl_statement_ifstatement;
    }

    public void setVhdl_statement_ifstatement(vhdl_statement_IfStatement vhdl_statement_ifstatement) {
        this.vhdl_statement_ifstatement = vhdl_statement_ifstatement;
    }
    public vhdl_statement_BlockStatement getVhdl_statement_blockstatement() {
        return vhdl_statement_blockstatement;
    }

    public void setVhdl_statement_blockstatement(vhdl_statement_BlockStatement vhdl_statement_blockstatement) {
        this.vhdl_statement_blockstatement = vhdl_statement_blockstatement;
    }
    public vhdl_statement_SimultaneousProceduralStatement getVhdl_statement_simultaneousproceduralstatement() {
        return vhdl_statement_simultaneousproceduralstatement;
    }

    public void setVhdl_statement_simultaneousproceduralstatement(vhdl_statement_SimultaneousProceduralStatement vhdl_statement_simultaneousproceduralstatement) {
        this.vhdl_statement_simultaneousproceduralstatement = vhdl_statement_simultaneousproceduralstatement;
    }
    public vhdl_statement_LoopStatement getVhdl_statement_loopstatement() {
        return vhdl_statement_loopstatement;
    }

    public void setVhdl_statement_loopstatement(vhdl_statement_LoopStatement vhdl_statement_loopstatement) {
        this.vhdl_statement_loopstatement = vhdl_statement_loopstatement;
    }
    public vhdl_statement_GenerateStatement getVhdl_statement_generatestatement() {
        return vhdl_statement_generatestatement;
    }

    public void setVhdl_statement_generatestatement(vhdl_statement_GenerateStatement vhdl_statement_generatestatement) {
        this.vhdl_statement_generatestatement = vhdl_statement_generatestatement;
    }

}