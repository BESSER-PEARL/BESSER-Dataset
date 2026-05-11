





import java.util.List;
import java.util.ArrayList;

public class myDsl_declaration_specifiers  {

    private String storage_class_specifier;
    private String function_specifier;





    private myDsl_function_definition mydsl_function_definition;




    private myDsl_declaration_specifiers mydsl_declaration_specifiers;




    private myDsl_declaration mydsl_declaration;


    public myDsl_declaration_specifiers(
        String storage_class_specifier,        String function_specifier    ) {
        this.storage_class_specifier = storage_class_specifier;
        this.function_specifier = function_specifier;
    }


    public String getStorage_class_specifier() {
        return storage_class_specifier;
    }

    public void setStorage_class_specifier(String storage_class_specifier) {
        this.storage_class_specifier = storage_class_specifier;
    }
    public String getFunction_specifier() {
        return function_specifier;
    }

    public void setFunction_specifier(String function_specifier) {
        this.function_specifier = function_specifier;
    }

    public myDsl_function_definition getMydsl_function_definition() {
        return mydsl_function_definition;
    }

    public void setMydsl_function_definition(myDsl_function_definition mydsl_function_definition) {
        this.mydsl_function_definition = mydsl_function_definition;
    }
    public myDsl_declaration_specifiers getMydsl_declaration_specifiers() {
        return mydsl_declaration_specifiers;
    }

    public void setMydsl_declaration_specifiers(myDsl_declaration_specifiers mydsl_declaration_specifiers) {
        this.mydsl_declaration_specifiers = mydsl_declaration_specifiers;
    }
    public myDsl_declaration getMydsl_declaration() {
        return mydsl_declaration;
    }

    public void setMydsl_declaration(myDsl_declaration mydsl_declaration) {
        this.mydsl_declaration = mydsl_declaration;
    }

}