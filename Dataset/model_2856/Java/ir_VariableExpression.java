





import java.util.List;
import java.util.ArrayList;

public class ir_VariableExpression extends Expression {






    private List<ir_Member> ir_members;




    private ir_Declaration ir_declaration;




    private List<ir_Expression> ir_expressions;


    public ir_VariableExpression(
    ) {
        super(
        );
        this.ir_members = new ArrayList<>();
        this.ir_expressions = new ArrayList<>();
    }

    public ir_VariableExpression(
        ArrayList<ir_Member> ir_members,        ArrayList<ir_Expression> ir_expressions    ) {
        this.ir_members = ir_members;
        this.ir_expressions = ir_expressions;
    }


    public List<ir_Member> getIr_members() {
        return ir_members;
    }

    public void addIr_member(Ir_member ir_member) {
        this.ir_members.add(ir_member);
    }
    public ir_Declaration getIr_declaration() {
        return ir_declaration;
    }

    public void setIr_declaration(ir_Declaration ir_declaration) {
        this.ir_declaration = ir_declaration;
    }
    public List<ir_Expression> getIr_expressions() {
        return ir_expressions;
    }

    public void addIr_expression(Ir_expression ir_expression) {
        this.ir_expressions.add(ir_expression);
    }

}