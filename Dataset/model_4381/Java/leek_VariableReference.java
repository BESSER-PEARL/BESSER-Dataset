





import java.util.List;
import java.util.ArrayList;

public class leek_VariableReference extends ForInVariableReference, AffectationPostfixStatement, Postfix {






    private List<leek_Expression> leek_expressions;




    private leek_Affectation leek_affectation;




    private leek_AffectationIncrement leek_affectationincrement;




    private leek_AffectationDecrement leek_affectationdecrement;




    private leek_VariableDeclaration leek_variabledeclaration;


    public leek_VariableReference(
    ) {
        super(
        );
        this.leek_expressions = new ArrayList<>();
    }

    public leek_VariableReference(
        ArrayList<leek_Expression> leek_expressions    ) {
        this.leek_expressions = leek_expressions;
    }


    public List<leek_Expression> getLeek_expressions() {
        return leek_expressions;
    }

    public void addLeek_expression(Leek_expression leek_expression) {
        this.leek_expressions.add(leek_expression);
    }
    public leek_Affectation getLeek_affectation() {
        return leek_affectation;
    }

    public void setLeek_affectation(leek_Affectation leek_affectation) {
        this.leek_affectation = leek_affectation;
    }
    public leek_AffectationIncrement getLeek_affectationincrement() {
        return leek_affectationincrement;
    }

    public void setLeek_affectationincrement(leek_AffectationIncrement leek_affectationincrement) {
        this.leek_affectationincrement = leek_affectationincrement;
    }
    public leek_AffectationDecrement getLeek_affectationdecrement() {
        return leek_affectationdecrement;
    }

    public void setLeek_affectationdecrement(leek_AffectationDecrement leek_affectationdecrement) {
        this.leek_affectationdecrement = leek_affectationdecrement;
    }
    public leek_VariableDeclaration getLeek_variabledeclaration() {
        return leek_variabledeclaration;
    }

    public void setLeek_variabledeclaration(leek_VariableDeclaration leek_variabledeclaration) {
        this.leek_variabledeclaration = leek_variabledeclaration;
    }

}