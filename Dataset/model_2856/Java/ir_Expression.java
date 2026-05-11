





import java.util.List;
import java.util.ArrayList;

public class ir_Expression extends Node {






    private ir_Scope ir_scope;




    private ir_Member ir_member;




    private ir_Variable ir_variable;




    private ir_VariableReference ir_variablereference;


    public ir_Expression(
    ) {
        super(
        );
    }



    public ir_Scope getIr_scope() {
        return ir_scope;
    }

    public void setIr_scope(ir_Scope ir_scope) {
        this.ir_scope = ir_scope;
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
    public ir_VariableReference getIr_variablereference() {
        return ir_variablereference;
    }

    public void setIr_variablereference(ir_VariableReference ir_variablereference) {
        this.ir_variablereference = ir_variablereference;
    }

}