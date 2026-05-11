





import java.util.List;
import java.util.ArrayList;

public class myDsl_parameter_declaration  {






    private myDsl_declaration_specifiers mydsl_declaration_specifiers;




    private myDsl_declarator mydsl_declarator;




    private myDsl_parameter_lista mydsl_parameter_lista;


    public myDsl_parameter_declaration(
    ) {
    }



    public myDsl_declaration_specifiers getMydsl_declaration_specifiers() {
        return mydsl_declaration_specifiers;
    }

    public void setMydsl_declaration_specifiers(myDsl_declaration_specifiers mydsl_declaration_specifiers) {
        this.mydsl_declaration_specifiers = mydsl_declaration_specifiers;
    }
    public myDsl_declarator getMydsl_declarator() {
        return mydsl_declarator;
    }

    public void setMydsl_declarator(myDsl_declarator mydsl_declarator) {
        this.mydsl_declarator = mydsl_declarator;
    }
    public myDsl_parameter_lista getMydsl_parameter_lista() {
        return mydsl_parameter_lista;
    }

    public void setMydsl_parameter_lista(myDsl_parameter_lista mydsl_parameter_lista) {
        this.mydsl_parameter_lista = mydsl_parameter_lista;
    }

}