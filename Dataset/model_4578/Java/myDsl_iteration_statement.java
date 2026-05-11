





import java.util.List;
import java.util.ArrayList;

public class myDsl_iteration_statement extends statement {






    private myDsl_declaration mydsl_declaration;


    public myDsl_iteration_statement(
    ) {
        super(
        );
    }



    public myDsl_declaration getMydsl_declaration() {
        return mydsl_declaration;
    }

    public void setMydsl_declaration(myDsl_declaration mydsl_declaration) {
        this.mydsl_declaration = mydsl_declaration;
    }

}