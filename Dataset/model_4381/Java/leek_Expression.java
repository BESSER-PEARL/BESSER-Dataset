





import java.util.List;
import java.util.ArrayList;

public class leek_Expression extends ForAffectation, IfCondition {






    private leek_ReturnStatement leek_returnstatement;




    private leek_AffectationDecrement leek_affectationdecrement;




    private leek_FunctionCall leek_functioncall;




    private leek_AffectationIncrement leek_affectationincrement;


    public leek_Expression(
    ) {
        super(
        );
    }



    public leek_ReturnStatement getLeek_returnstatement() {
        return leek_returnstatement;
    }

    public void setLeek_returnstatement(leek_ReturnStatement leek_returnstatement) {
        this.leek_returnstatement = leek_returnstatement;
    }
    public leek_AffectationDecrement getLeek_affectationdecrement() {
        return leek_affectationdecrement;
    }

    public void setLeek_affectationdecrement(leek_AffectationDecrement leek_affectationdecrement) {
        this.leek_affectationdecrement = leek_affectationdecrement;
    }
    public leek_FunctionCall getLeek_functioncall() {
        return leek_functioncall;
    }

    public void setLeek_functioncall(leek_FunctionCall leek_functioncall) {
        this.leek_functioncall = leek_functioncall;
    }
    public leek_AffectationIncrement getLeek_affectationincrement() {
        return leek_affectationincrement;
    }

    public void setLeek_affectationincrement(leek_AffectationIncrement leek_affectationincrement) {
        this.leek_affectationincrement = leek_affectationincrement;
    }

}