





import java.util.List;
import java.util.ArrayList;

public class myDsl_DeclarationListLinhaAction extends declaration_list_linha {






    private myDsl_declaration mydsl_declaration;




    private myDsl_declaration_list_linha mydsl_declaration_list_linha;


    public myDsl_DeclarationListLinhaAction(
    ) {
        super(
        );
    }



    public myDsl_declaration getMydsl_declaration() {
        return mydsl_declaration;
    }

    public void setMydsl_declaration(myDsl_declaration mydsl_declaration) {
        this.mydsl_declaration = mydsl_declaration;
    }
    public myDsl_declaration_list_linha getMydsl_declaration_list_linha() {
        return mydsl_declaration_list_linha;
    }

    public void setMydsl_declaration_list_linha(myDsl_declaration_list_linha mydsl_declaration_list_linha) {
        this.mydsl_declaration_list_linha = mydsl_declaration_list_linha;
    }

}