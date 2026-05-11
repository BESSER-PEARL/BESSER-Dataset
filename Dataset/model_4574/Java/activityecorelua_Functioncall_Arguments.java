





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_Functioncall_Arguments  {






    private activityecorelua_Expression_CallMemberFunction activityecorelua_expression_callmemberfunction;




    private activityecorelua_Statement_CallFunction activityecorelua_statement_callfunction;




    private List<activityecorelua_Expression> activityecorelua_expressions;




    private activityecorelua_Expression_CallFunction activityecorelua_expression_callfunction;




    private activityecorelua_Statement_CallMemberFunction activityecorelua_statement_callmemberfunction;


    public activityecorelua_Functioncall_Arguments(
    ) {
        this.activityecorelua_expressions = new ArrayList<>();
    }

    public activityecorelua_Functioncall_Arguments(
        ArrayList<activityecorelua_Expression> activityecorelua_expressions    ) {
        this.activityecorelua_expressions = activityecorelua_expressions;
    }


    public activityecorelua_Expression_CallMemberFunction getActivityecorelua_expression_callmemberfunction() {
        return activityecorelua_expression_callmemberfunction;
    }

    public void setActivityecorelua_expression_callmemberfunction(activityecorelua_Expression_CallMemberFunction activityecorelua_expression_callmemberfunction) {
        this.activityecorelua_expression_callmemberfunction = activityecorelua_expression_callmemberfunction;
    }
    public activityecorelua_Statement_CallFunction getActivityecorelua_statement_callfunction() {
        return activityecorelua_statement_callfunction;
    }

    public void setActivityecorelua_statement_callfunction(activityecorelua_Statement_CallFunction activityecorelua_statement_callfunction) {
        this.activityecorelua_statement_callfunction = activityecorelua_statement_callfunction;
    }
    public List<activityecorelua_Expression> getActivityecorelua_expressions() {
        return activityecorelua_expressions;
    }

    public void addActivityecorelua_expression(Activityecorelua_expression activityecorelua_expression) {
        this.activityecorelua_expressions.add(activityecorelua_expression);
    }
    public activityecorelua_Expression_CallFunction getActivityecorelua_expression_callfunction() {
        return activityecorelua_expression_callfunction;
    }

    public void setActivityecorelua_expression_callfunction(activityecorelua_Expression_CallFunction activityecorelua_expression_callfunction) {
        this.activityecorelua_expression_callfunction = activityecorelua_expression_callfunction;
    }
    public activityecorelua_Statement_CallMemberFunction getActivityecorelua_statement_callmemberfunction() {
        return activityecorelua_statement_callmemberfunction;
    }

    public void setActivityecorelua_statement_callmemberfunction(activityecorelua_Statement_CallMemberFunction activityecorelua_statement_callmemberfunction) {
        this.activityecorelua_statement_callmemberfunction = activityecorelua_statement_callmemberfunction;
    }

}