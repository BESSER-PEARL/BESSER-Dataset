





import java.util.List;
import java.util.ArrayList;

public class vhdl_SubtypeIndication  {

    private String builtin_type;





    private vhdl_ConstantDeclaration vhdl_constantdeclaration;




    private vhdl_Type vhdl_type;




    private vhdl_Port vhdl_port;




    private vhdl_SignalDeclaration vhdl_signaldeclaration;




    private vhdl_Generic vhdl_generic;




    private vhdl_VariableDeclaration vhdl_variabledeclaration;




    private vhdl_Expression vhdl_expression;




    private vhdl_Alias vhdl_alias;


    public vhdl_SubtypeIndication(
        String builtin_type    ) {
        this.builtin_type = builtin_type;
    }


    public String getBuiltin_type() {
        return builtin_type;
    }

    public void setBuiltin_type(String builtin_type) {
        this.builtin_type = builtin_type;
    }

    public vhdl_ConstantDeclaration getVhdl_constantdeclaration() {
        return vhdl_constantdeclaration;
    }

    public void setVhdl_constantdeclaration(vhdl_ConstantDeclaration vhdl_constantdeclaration) {
        this.vhdl_constantdeclaration = vhdl_constantdeclaration;
    }
    public vhdl_Type getVhdl_type() {
        return vhdl_type;
    }

    public void setVhdl_type(vhdl_Type vhdl_type) {
        this.vhdl_type = vhdl_type;
    }
    public vhdl_Port getVhdl_port() {
        return vhdl_port;
    }

    public void setVhdl_port(vhdl_Port vhdl_port) {
        this.vhdl_port = vhdl_port;
    }
    public vhdl_SignalDeclaration getVhdl_signaldeclaration() {
        return vhdl_signaldeclaration;
    }

    public void setVhdl_signaldeclaration(vhdl_SignalDeclaration vhdl_signaldeclaration) {
        this.vhdl_signaldeclaration = vhdl_signaldeclaration;
    }
    public vhdl_Generic getVhdl_generic() {
        return vhdl_generic;
    }

    public void setVhdl_generic(vhdl_Generic vhdl_generic) {
        this.vhdl_generic = vhdl_generic;
    }
    public vhdl_VariableDeclaration getVhdl_variabledeclaration() {
        return vhdl_variabledeclaration;
    }

    public void setVhdl_variabledeclaration(vhdl_VariableDeclaration vhdl_variabledeclaration) {
        this.vhdl_variabledeclaration = vhdl_variabledeclaration;
    }
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }
    public vhdl_Alias getVhdl_alias() {
        return vhdl_alias;
    }

    public void setVhdl_alias(vhdl_Alias vhdl_alias) {
        this.vhdl_alias = vhdl_alias;
    }

}