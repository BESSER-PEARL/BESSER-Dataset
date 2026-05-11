





import java.util.List;
import java.util.ArrayList;

public class dom_ModelDeclarationStatement extends Statement {






    private dom_NameExpression dom_nameexpression;




    private dom_NameExpression dom_nameexpression;




    private List<dom_NameExpression> dom_nameexpressions;




    private dom_Program dom_program;




    private List<dom_ModelDeclarationParameter> dom_modeldeclarationparameters;


    public dom_ModelDeclarationStatement(
    ) {
        super(
        );
        this.dom_nameexpressions = new ArrayList<>();
        this.dom_modeldeclarationparameters = new ArrayList<>();
    }

    public dom_ModelDeclarationStatement(
        ArrayList<dom_NameExpression> dom_nameexpressions,        ArrayList<dom_ModelDeclarationParameter> dom_modeldeclarationparameters    ) {
        this.dom_nameexpressions = dom_nameexpressions;
        this.dom_modeldeclarationparameters = dom_modeldeclarationparameters;
    }


    public dom_NameExpression getDom_nameexpression() {
        return dom_nameexpression;
    }

    public void setDom_nameexpression(dom_NameExpression dom_nameexpression) {
        this.dom_nameexpression = dom_nameexpression;
    }
    public dom_NameExpression getDom_nameexpression() {
        return dom_nameexpression;
    }

    public void setDom_nameexpression(dom_NameExpression dom_nameexpression) {
        this.dom_nameexpression = dom_nameexpression;
    }
    public List<dom_NameExpression> getDom_nameexpressions() {
        return dom_nameexpressions;
    }

    public void addDom_nameexpression(Dom_nameexpression dom_nameexpression) {
        this.dom_nameexpressions.add(dom_nameexpression);
    }
    public dom_Program getDom_program() {
        return dom_program;
    }

    public void setDom_program(dom_Program dom_program) {
        this.dom_program = dom_program;
    }
    public List<dom_ModelDeclarationParameter> getDom_modeldeclarationparameters() {
        return dom_modeldeclarationparameters;
    }

    public void addDom_modeldeclarationparameter(Dom_modeldeclarationparameter dom_modeldeclarationparameter) {
        this.dom_modeldeclarationparameters.add(dom_modeldeclarationparameter);
    }

}