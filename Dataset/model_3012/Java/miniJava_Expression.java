





import java.util.List;
import java.util.ArrayList;

public class miniJava_Expression extends Statement, Assignee {






    private miniJava_Assignment minijava_assignment;




    private miniJava_ForStatement minijava_forstatement;




    private miniJava_Field minijava_field;




    private miniJava_WhileStatement minijava_whilestatement;


    public miniJava_Expression(
    ) {
        super(
        );
    }



    public miniJava_Assignment getMinijava_assignment() {
        return minijava_assignment;
    }

    public void setMinijava_assignment(miniJava_Assignment minijava_assignment) {
        this.minijava_assignment = minijava_assignment;
    }
    public miniJava_ForStatement getMinijava_forstatement() {
        return minijava_forstatement;
    }

    public void setMinijava_forstatement(miniJava_ForStatement minijava_forstatement) {
        this.minijava_forstatement = minijava_forstatement;
    }
    public miniJava_Field getMinijava_field() {
        return minijava_field;
    }

    public void setMinijava_field(miniJava_Field minijava_field) {
        this.minijava_field = minijava_field;
    }
    public miniJava_WhileStatement getMinijava_whilestatement() {
        return minijava_whilestatement;
    }

    public void setMinijava_whilestatement(miniJava_WhileStatement minijava_whilestatement) {
        this.minijava_whilestatement = minijava_whilestatement;
    }

}