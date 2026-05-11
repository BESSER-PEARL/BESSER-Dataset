





import java.util.List;
import java.util.ArrayList;

public class myDsl_alignment_specifier  {

    private String alignas;





    private myDsl_type_name mydsl_type_name;




    private myDsl_declaration_specifiers mydsl_declaration_specifiers;




    private myDsl_constant_expression mydsl_constant_expression;


    public myDsl_alignment_specifier(
        String alignas    ) {
        this.alignas = alignas;
    }


    public String getAlignas() {
        return alignas;
    }

    public void setAlignas(String alignas) {
        this.alignas = alignas;
    }

    public myDsl_type_name getMydsl_type_name() {
        return mydsl_type_name;
    }

    public void setMydsl_type_name(myDsl_type_name mydsl_type_name) {
        this.mydsl_type_name = mydsl_type_name;
    }
    public myDsl_declaration_specifiers getMydsl_declaration_specifiers() {
        return mydsl_declaration_specifiers;
    }

    public void setMydsl_declaration_specifiers(myDsl_declaration_specifiers mydsl_declaration_specifiers) {
        this.mydsl_declaration_specifiers = mydsl_declaration_specifiers;
    }
    public myDsl_constant_expression getMydsl_constant_expression() {
        return mydsl_constant_expression;
    }

    public void setMydsl_constant_expression(myDsl_constant_expression mydsl_constant_expression) {
        this.mydsl_constant_expression = mydsl_constant_expression;
    }

}