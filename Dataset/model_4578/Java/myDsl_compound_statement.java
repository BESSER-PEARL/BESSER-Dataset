





import java.util.List;
import java.util.ArrayList;

public class myDsl_compound_statement extends statement {






    private myDsl_function_definition mydsl_function_definition;


    public myDsl_compound_statement(
    ) {
        super(
        );
    }



    public myDsl_function_definition getMydsl_function_definition() {
        return mydsl_function_definition;
    }

    public void setMydsl_function_definition(myDsl_function_definition mydsl_function_definition) {
        this.mydsl_function_definition = mydsl_function_definition;
    }

}