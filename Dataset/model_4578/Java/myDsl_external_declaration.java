





import java.util.List;
import java.util.ArrayList;

public class myDsl_external_declaration  {






    private myDsl_declaration_specifiers mydsl_declaration_specifiers;




    private myDsl_translation_unit mydsl_translation_unit;




    private myDsl_translation_unitR mydsl_translation_unitr;


    public myDsl_external_declaration(
    ) {
    }



    public myDsl_declaration_specifiers getMydsl_declaration_specifiers() {
        return mydsl_declaration_specifiers;
    }

    public void setMydsl_declaration_specifiers(myDsl_declaration_specifiers mydsl_declaration_specifiers) {
        this.mydsl_declaration_specifiers = mydsl_declaration_specifiers;
    }
    public myDsl_translation_unit getMydsl_translation_unit() {
        return mydsl_translation_unit;
    }

    public void setMydsl_translation_unit(myDsl_translation_unit mydsl_translation_unit) {
        this.mydsl_translation_unit = mydsl_translation_unit;
    }
    public myDsl_translation_unitR getMydsl_translation_unitr() {
        return mydsl_translation_unitr;
    }

    public void setMydsl_translation_unitr(myDsl_translation_unitR mydsl_translation_unitr) {
        this.mydsl_translation_unitr = mydsl_translation_unitr;
    }

}