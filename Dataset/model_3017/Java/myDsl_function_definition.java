





import java.util.List;
import java.util.ArrayList;

public class myDsl_function_definition  {






    private myDsl_compound_statement mydsl_compound_statement;




    private myDsl_declarator mydsl_declarator;




    private myDsl_declaration_specifiers mydsl_declaration_specifiers;


    public myDsl_function_definition(
    ) {
    }



    public myDsl_compound_statement getMydsl_compound_statement() {
        return mydsl_compound_statement;
    }

    public void setMydsl_compound_statement(myDsl_compound_statement mydsl_compound_statement) {
        this.mydsl_compound_statement = mydsl_compound_statement;
    }
    public myDsl_declarator getMydsl_declarator() {
        return mydsl_declarator;
    }

    public void setMydsl_declarator(myDsl_declarator mydsl_declarator) {
        this.mydsl_declarator = mydsl_declarator;
    }
    public myDsl_declaration_specifiers getMydsl_declaration_specifiers() {
        return mydsl_declaration_specifiers;
    }

    public void setMydsl_declaration_specifiers(myDsl_declaration_specifiers mydsl_declaration_specifiers) {
        this.mydsl_declaration_specifiers = mydsl_declaration_specifiers;
    }

}