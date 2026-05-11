





import java.util.List;
import java.util.ArrayList;

public class iot2_Functioncall_Arguments  {






    private iot2_Statement_CallFunction iot2_statement_callfunction;




    private List<iot2_Expression> iot2_expressions;




    private iot2_Expression_CallMemberFunction iot2_expression_callmemberfunction;




    private iot2_Expression_CallFunction iot2_expression_callfunction;




    private iot2_Statement_CallMemberFunction iot2_statement_callmemberfunction;


    public iot2_Functioncall_Arguments(
    ) {
        this.iot2_expressions = new ArrayList<>();
    }

    public iot2_Functioncall_Arguments(
        ArrayList<iot2_Expression> iot2_expressions    ) {
        this.iot2_expressions = iot2_expressions;
    }


    public iot2_Statement_CallFunction getIot2_statement_callfunction() {
        return iot2_statement_callfunction;
    }

    public void setIot2_statement_callfunction(iot2_Statement_CallFunction iot2_statement_callfunction) {
        this.iot2_statement_callfunction = iot2_statement_callfunction;
    }
    public List<iot2_Expression> getIot2_expressions() {
        return iot2_expressions;
    }

    public void addIot2_expression(Iot2_expression iot2_expression) {
        this.iot2_expressions.add(iot2_expression);
    }
    public iot2_Expression_CallMemberFunction getIot2_expression_callmemberfunction() {
        return iot2_expression_callmemberfunction;
    }

    public void setIot2_expression_callmemberfunction(iot2_Expression_CallMemberFunction iot2_expression_callmemberfunction) {
        this.iot2_expression_callmemberfunction = iot2_expression_callmemberfunction;
    }
    public iot2_Expression_CallFunction getIot2_expression_callfunction() {
        return iot2_expression_callfunction;
    }

    public void setIot2_expression_callfunction(iot2_Expression_CallFunction iot2_expression_callfunction) {
        this.iot2_expression_callfunction = iot2_expression_callfunction;
    }
    public iot2_Statement_CallMemberFunction getIot2_statement_callmemberfunction() {
        return iot2_statement_callmemberfunction;
    }

    public void setIot2_statement_callmemberfunction(iot2_Statement_CallMemberFunction iot2_statement_callmemberfunction) {
        this.iot2_statement_callmemberfunction = iot2_statement_callmemberfunction;
    }

}