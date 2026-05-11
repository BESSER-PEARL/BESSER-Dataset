





import java.util.List;
import java.util.ArrayList;

public class ansic_assignment_expression  {

    private String assignment_operator;





    private ansic_initializer ansic_initializer;




    private ansic_direct_declarator_complemento ansic_direct_declarator_complemento;




    private ansic_direct_abstract_declarator ansic_direct_abstract_declarator;




    private ansic_direct_abstract_declarator_complement ansic_direct_abstract_declarator_complement;




    private ansic_assignment_expression ansic_assignment_expression;


    public ansic_assignment_expression(
        String assignment_operator    ) {
        this.assignment_operator = assignment_operator;
    }


    public String getAssignment_operator() {
        return assignment_operator;
    }

    public void setAssignment_operator(String assignment_operator) {
        this.assignment_operator = assignment_operator;
    }

    public ansic_initializer getAnsic_initializer() {
        return ansic_initializer;
    }

    public void setAnsic_initializer(ansic_initializer ansic_initializer) {
        this.ansic_initializer = ansic_initializer;
    }
    public ansic_direct_declarator_complemento getAnsic_direct_declarator_complemento() {
        return ansic_direct_declarator_complemento;
    }

    public void setAnsic_direct_declarator_complemento(ansic_direct_declarator_complemento ansic_direct_declarator_complemento) {
        this.ansic_direct_declarator_complemento = ansic_direct_declarator_complemento;
    }
    public ansic_direct_abstract_declarator getAnsic_direct_abstract_declarator() {
        return ansic_direct_abstract_declarator;
    }

    public void setAnsic_direct_abstract_declarator(ansic_direct_abstract_declarator ansic_direct_abstract_declarator) {
        this.ansic_direct_abstract_declarator = ansic_direct_abstract_declarator;
    }
    public ansic_direct_abstract_declarator_complement getAnsic_direct_abstract_declarator_complement() {
        return ansic_direct_abstract_declarator_complement;
    }

    public void setAnsic_direct_abstract_declarator_complement(ansic_direct_abstract_declarator_complement ansic_direct_abstract_declarator_complement) {
        this.ansic_direct_abstract_declarator_complement = ansic_direct_abstract_declarator_complement;
    }
    public ansic_assignment_expression getAnsic_assignment_expression() {
        return ansic_assignment_expression;
    }

    public void setAnsic_assignment_expression(ansic_assignment_expression ansic_assignment_expression) {
        this.ansic_assignment_expression = ansic_assignment_expression;
    }

}