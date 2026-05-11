





import java.util.List;
import java.util.ArrayList;

public class myDsl_external_declaration  {






    private myDsl_translation_unit mydsl_translation_unit;




    private myDsl_function_definition mydsl_function_definition;




    private myDsl_declaration mydsl_declaration;


    public myDsl_external_declaration(
    ) {
    }



    public myDsl_translation_unit getMydsl_translation_unit() {
        return mydsl_translation_unit;
    }

    public void setMydsl_translation_unit(myDsl_translation_unit mydsl_translation_unit) {
        this.mydsl_translation_unit = mydsl_translation_unit;
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