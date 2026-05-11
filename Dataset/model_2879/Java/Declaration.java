





import java.util.List;
import java.util.ArrayList;

public class Declaration  {






    private vhdl_statement_SimultaneousProceduralStatement vhdl_statement_simultaneousproceduralstatement;




    private vhdl_declaration_SubprogramBody vhdl_declaration_subprogrambody;




    private vhdl_Ports vhdl_ports;




    private vhdl_statement_GenerateStatement vhdl_statement_generatestatement;




    private vhdl_statement_ProcessStatement vhdl_statement_processstatement;




    private vhdl_declaration_SubprogramDeclaration vhdl_declaration_subprogramdeclaration;




    private vhdl_Module vhdl_module;




    private vhdl_statement_BlockStatement vhdl_statement_blockstatement;




    private vhdl_Generics vhdl_generics;


    public Declaration(
    ) {
    }



    public vhdl_statement_SimultaneousProceduralStatement getVhdl_statement_simultaneousproceduralstatement() {
        return vhdl_statement_simultaneousproceduralstatement;
    }

    public void setVhdl_statement_simultaneousproceduralstatement(vhdl_statement_SimultaneousProceduralStatement vhdl_statement_simultaneousproceduralstatement) {
        this.vhdl_statement_simultaneousproceduralstatement = vhdl_statement_simultaneousproceduralstatement;
    }
    public vhdl_declaration_SubprogramBody getVhdl_declaration_subprogrambody() {
        return vhdl_declaration_subprogrambody;
    }

    public void setVhdl_declaration_subprogrambody(vhdl_declaration_SubprogramBody vhdl_declaration_subprogrambody) {
        this.vhdl_declaration_subprogrambody = vhdl_declaration_subprogrambody;
    }
    public vhdl_Ports getVhdl_ports() {
        return vhdl_ports;
    }

    public void setVhdl_ports(vhdl_Ports vhdl_ports) {
        this.vhdl_ports = vhdl_ports;
    }
    public vhdl_statement_GenerateStatement getVhdl_statement_generatestatement() {
        return vhdl_statement_generatestatement;
    }

    public void setVhdl_statement_generatestatement(vhdl_statement_GenerateStatement vhdl_statement_generatestatement) {
        this.vhdl_statement_generatestatement = vhdl_statement_generatestatement;
    }
    public vhdl_statement_ProcessStatement getVhdl_statement_processstatement() {
        return vhdl_statement_processstatement;
    }

    public void setVhdl_statement_processstatement(vhdl_statement_ProcessStatement vhdl_statement_processstatement) {
        this.vhdl_statement_processstatement = vhdl_statement_processstatement;
    }
    public vhdl_declaration_SubprogramDeclaration getVhdl_declaration_subprogramdeclaration() {
        return vhdl_declaration_subprogramdeclaration;
    }

    public void setVhdl_declaration_subprogramdeclaration(vhdl_declaration_SubprogramDeclaration vhdl_declaration_subprogramdeclaration) {
        this.vhdl_declaration_subprogramdeclaration = vhdl_declaration_subprogramdeclaration;
    }
    public vhdl_Module getVhdl_module() {
        return vhdl_module;
    }

    public void setVhdl_module(vhdl_Module vhdl_module) {
        this.vhdl_module = vhdl_module;
    }
    public vhdl_statement_BlockStatement getVhdl_statement_blockstatement() {
        return vhdl_statement_blockstatement;
    }

    public void setVhdl_statement_blockstatement(vhdl_statement_BlockStatement vhdl_statement_blockstatement) {
        this.vhdl_statement_blockstatement = vhdl_statement_blockstatement;
    }
    public vhdl_Generics getVhdl_generics() {
        return vhdl_generics;
    }

    public void setVhdl_generics(vhdl_Generics vhdl_generics) {
        this.vhdl_generics = vhdl_generics;
    }

}