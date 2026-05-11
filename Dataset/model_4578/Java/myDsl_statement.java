





import java.util.List;
import java.util.ArrayList;

public class myDsl_statement extends block_item {






    private myDsl_labeled_statement mydsl_labeled_statement;




    private myDsl_IDENTIFIER mydsl_identifier;




    private myDsl_labeled_statement mydsl_labeled_statement;




    private myDsl_selection_statement mydsl_selection_statement;




    private myDsl_iteration_statement mydsl_iteration_statement;


    public myDsl_statement(
    ) {
        super(
        );
    }



    public myDsl_labeled_statement getMydsl_labeled_statement() {
        return mydsl_labeled_statement;
    }

    public void setMydsl_labeled_statement(myDsl_labeled_statement mydsl_labeled_statement) {
        this.mydsl_labeled_statement = mydsl_labeled_statement;
    }
    public myDsl_IDENTIFIER getMydsl_identifier() {
        return mydsl_identifier;
    }

    public void setMydsl_identifier(myDsl_IDENTIFIER mydsl_identifier) {
        this.mydsl_identifier = mydsl_identifier;
    }
    public myDsl_labeled_statement getMydsl_labeled_statement() {
        return mydsl_labeled_statement;
    }

    public void setMydsl_labeled_statement(myDsl_labeled_statement mydsl_labeled_statement) {
        this.mydsl_labeled_statement = mydsl_labeled_statement;
    }
    public myDsl_selection_statement getMydsl_selection_statement() {
        return mydsl_selection_statement;
    }

    public void setMydsl_selection_statement(myDsl_selection_statement mydsl_selection_statement) {
        this.mydsl_selection_statement = mydsl_selection_statement;
    }
    public myDsl_iteration_statement getMydsl_iteration_statement() {
        return mydsl_iteration_statement;
    }

    public void setMydsl_iteration_statement(myDsl_iteration_statement mydsl_iteration_statement) {
        this.mydsl_iteration_statement = mydsl_iteration_statement;
    }

}