





import java.util.List;
import java.util.ArrayList;

public class ir_Type  {






    private ir_TypeDeclaration ir_typedeclaration;




    private ir_VariableExternal ir_variableexternal;




    private ir_ForwardDeclaration ir_forwarddeclaration;




    private ir_Member ir_member;




    private ir_Variable ir_variable;




    private ir_Expression ir_expression;




    private ir_VariableReference ir_variablereference;




    private ir_Port ir_port;


    public ir_Type(
    ) {
    }



    public ir_TypeDeclaration getIr_typedeclaration() {
        return ir_typedeclaration;
    }

    public void setIr_typedeclaration(ir_TypeDeclaration ir_typedeclaration) {
        this.ir_typedeclaration = ir_typedeclaration;
    }
    public ir_VariableExternal getIr_variableexternal() {
        return ir_variableexternal;
    }

    public void setIr_variableexternal(ir_VariableExternal ir_variableexternal) {
        this.ir_variableexternal = ir_variableexternal;
    }
    public ir_ForwardDeclaration getIr_forwarddeclaration() {
        return ir_forwarddeclaration;
    }

    public void setIr_forwarddeclaration(ir_ForwardDeclaration ir_forwarddeclaration) {
        this.ir_forwarddeclaration = ir_forwarddeclaration;
    }
    public ir_Member getIr_member() {
        return ir_member;
    }

    public void setIr_member(ir_Member ir_member) {
        this.ir_member = ir_member;
    }
    public ir_Variable getIr_variable() {
        return ir_variable;
    }

    public void setIr_variable(ir_Variable ir_variable) {
        this.ir_variable = ir_variable;
    }
    public ir_Expression getIr_expression() {
        return ir_expression;
    }

    public void setIr_expression(ir_Expression ir_expression) {
        this.ir_expression = ir_expression;
    }
    public ir_VariableReference getIr_variablereference() {
        return ir_variablereference;
    }

    public void setIr_variablereference(ir_VariableReference ir_variablereference) {
        this.ir_variablereference = ir_variablereference;
    }
    public ir_Port getIr_port() {
        return ir_port;
    }

    public void setIr_port(ir_Port ir_port) {
        this.ir_port = ir_port;
    }

}