





import java.util.List;
import java.util.ArrayList;

public class myDsl_declaration_list  {






    private myDsl_function_definition mydsl_function_definition;




    private myDsl_declaration mydsl_declaration;


    public myDsl_declaration_list(
    ) {
    }



    public myDsl_function_definition getMydsl_function_definition() {
        return mydsl_function_definition;
    }

    public void setMydsl_function_definition(myDsl_function_definition mydsl_function_definition) {
        this.mydsl_function_definition = mydsl_function_definition;
    }
    public myDsl_declaration getMydsl_declaration() {
        return mydsl_declaration;
    }

    public void setMydsl_declaration(myDsl_declaration mydsl_declaration) {
        this.mydsl_declaration = mydsl_declaration;
    }

}