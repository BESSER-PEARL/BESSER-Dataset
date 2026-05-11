





import java.util.List;
import java.util.ArrayList;

public class myDsl_Variable  {

    private String variable;





    private myDsl_Affectation mydsl_affectation;


    public myDsl_Variable(
        String variable    ) {
        this.variable = variable;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public myDsl_Affectation getMydsl_affectation() {
        return mydsl_affectation;
    }

    public void setMydsl_affectation(myDsl_Affectation mydsl_affectation) {
        this.mydsl_affectation = mydsl_affectation;
    }

}