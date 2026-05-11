





import java.util.List;
import java.util.ArrayList;

public class myDsl_declarator  {






    private myDsl_function_definition mydsl_function_definition;




    private myDsl_struct_declarator mydsl_struct_declarator;


    public myDsl_declarator(
    ) {
    }



    public myDsl_function_definition getMydsl_function_definition() {
        return mydsl_function_definition;
    }

    public void setMydsl_function_definition(myDsl_function_definition mydsl_function_definition) {
        this.mydsl_function_definition = mydsl_function_definition;
    }
    public myDsl_struct_declarator getMydsl_struct_declarator() {
        return mydsl_struct_declarator;
    }

    public void setMydsl_struct_declarator(myDsl_struct_declarator mydsl_struct_declarator) {
        this.mydsl_struct_declarator = mydsl_struct_declarator;
    }

}