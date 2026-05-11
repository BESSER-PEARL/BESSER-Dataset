





import java.util.List;
import java.util.ArrayList;

public class myDsl_assignment_expression  {

    private String assignment_operator;





    private myDsl_direct_declarator_complemento mydsl_direct_declarator_complemento;




    private myDsl_assignment_expression mydsl_assignment_expression;




    private myDsl_generic_association mydsl_generic_association;




    private myDsl_conditional_expression mydsl_conditional_expression;




    private myDsl_generic_selection mydsl_generic_selection;




    private myDsl_expression mydsl_expression;




    private myDsl_unary_expression mydsl_unary_expression;




    private myDsl_argument_expression_list mydsl_argument_expression_list;


    public myDsl_assignment_expression(
        String assignment_operator    ) {
        this.assignment_operator = assignment_operator;
    }


    public String getAssignment_operator() {
        return assignment_operator;
    }

    public void setAssignment_operator(String assignment_operator) {
        this.assignment_operator = assignment_operator;
    }

    public myDsl_direct_declarator_complemento getMydsl_direct_declarator_complemento() {
        return mydsl_direct_declarator_complemento;
    }

    public void setMydsl_direct_declarator_complemento(myDsl_direct_declarator_complemento mydsl_direct_declarator_complemento) {
        this.mydsl_direct_declarator_complemento = mydsl_direct_declarator_complemento;
    }
    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }
    public myDsl_generic_association getMydsl_generic_association() {
        return mydsl_generic_association;
    }

    public void setMydsl_generic_association(myDsl_generic_association mydsl_generic_association) {
        this.mydsl_generic_association = mydsl_generic_association;
    }
    public myDsl_conditional_expression getMydsl_conditional_expression() {
        return mydsl_conditional_expression;
    }

    public void setMydsl_conditional_expression(myDsl_conditional_expression mydsl_conditional_expression) {
        this.mydsl_conditional_expression = mydsl_conditional_expression;
    }
    public myDsl_generic_selection getMydsl_generic_selection() {
        return mydsl_generic_selection;
    }

    public void setMydsl_generic_selection(myDsl_generic_selection mydsl_generic_selection) {
        this.mydsl_generic_selection = mydsl_generic_selection;
    }
    public myDsl_expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_unary_expression getMydsl_unary_expression() {
        return mydsl_unary_expression;
    }

    public void setMydsl_unary_expression(myDsl_unary_expression mydsl_unary_expression) {
        this.mydsl_unary_expression = mydsl_unary_expression;
    }
    public myDsl_argument_expression_list getMydsl_argument_expression_list() {
        return mydsl_argument_expression_list;
    }

    public void setMydsl_argument_expression_list(myDsl_argument_expression_list mydsl_argument_expression_list) {
        this.mydsl_argument_expression_list = mydsl_argument_expression_list;
    }

}