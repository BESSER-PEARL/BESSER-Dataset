





import java.util.List;
import java.util.ArrayList;

public class miniJava_Expression extends Assignee, Statement {






    private miniJava_PrintStatement minijava_printstatement;




    private miniJava_Assignment minijava_assignment;




    private miniJava_WhileStatement minijava_whilestatement;




    private miniJava_Field minijava_field;


    public miniJava_Expression(
    ) {
        super(
        );
    }



    public miniJava_PrintStatement getMinijava_printstatement() {
        return minijava_printstatement;
    }

    public void setMinijava_printstatement(miniJava_PrintStatement minijava_printstatement) {
        this.minijava_printstatement = minijava_printstatement;
    }
    public miniJava_Assignment getMinijava_assignment() {
        return minijava_assignment;
    }

    public void setMinijava_assignment(miniJava_Assignment minijava_assignment) {
        this.minijava_assignment = minijava_assignment;
    }
    public miniJava_WhileStatement getMinijava_whilestatement() {
        return minijava_whilestatement;
    }

    public void setMinijava_whilestatement(miniJava_WhileStatement minijava_whilestatement) {
        this.minijava_whilestatement = minijava_whilestatement;
    }
    public miniJava_Field getMinijava_field() {
        return minijava_field;
    }

    public void setMinijava_field(miniJava_Field minijava_field) {
        this.minijava_field = minijava_field;
    }

}