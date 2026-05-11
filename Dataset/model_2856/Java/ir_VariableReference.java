





import java.util.List;
import java.util.ArrayList;

public class ir_VariableReference extends Node {






    private ir_Variable ir_variable;




    private List<ir_Member> ir_members;


    public ir_VariableReference(
    ) {
        super(
        );
        this.ir_members = new ArrayList<>();
    }

    public ir_VariableReference(
        ArrayList<ir_Member> ir_members    ) {
        this.ir_members = ir_members;
    }


    public ir_Variable getIr_variable() {
        return ir_variable;
    }

    public void setIr_variable(ir_Variable ir_variable) {
        this.ir_variable = ir_variable;
    }
    public List<ir_Member> getIr_members() {
        return ir_members;
    }

    public void addIr_member(Ir_member ir_member) {
        this.ir_members.add(ir_member);
    }

}