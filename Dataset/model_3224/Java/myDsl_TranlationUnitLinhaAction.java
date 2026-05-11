





import java.util.List;
import java.util.ArrayList;

public class myDsl_TranlationUnitLinhaAction extends translation_unit_linha {






    private myDsl_external_declaration mydsl_external_declaration;




    private myDsl_translation_unit_linha mydsl_translation_unit_linha;


    public myDsl_TranlationUnitLinhaAction(
    ) {
        super(
        );
    }



    public myDsl_external_declaration getMydsl_external_declaration() {
        return mydsl_external_declaration;
    }

    public void setMydsl_external_declaration(myDsl_external_declaration mydsl_external_declaration) {
        this.mydsl_external_declaration = mydsl_external_declaration;
    }
    public myDsl_translation_unit_linha getMydsl_translation_unit_linha() {
        return mydsl_translation_unit_linha;
    }

    public void setMydsl_translation_unit_linha(myDsl_translation_unit_linha mydsl_translation_unit_linha) {
        this.mydsl_translation_unit_linha = mydsl_translation_unit_linha;
    }

}