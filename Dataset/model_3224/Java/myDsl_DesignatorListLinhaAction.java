





import java.util.List;
import java.util.ArrayList;

public class myDsl_DesignatorListLinhaAction extends designator_list_linha {






    private myDsl_declaration_list_linha mydsl_declaration_list_linha;




    private myDsl_designator mydsl_designator;


    public myDsl_DesignatorListLinhaAction(
    ) {
        super(
        );
    }



    public myDsl_declaration_list_linha getMydsl_declaration_list_linha() {
        return mydsl_declaration_list_linha;
    }

    public void setMydsl_declaration_list_linha(myDsl_declaration_list_linha mydsl_declaration_list_linha) {
        this.mydsl_declaration_list_linha = mydsl_declaration_list_linha;
    }
    public myDsl_designator getMydsl_designator() {
        return mydsl_designator;
    }

    public void setMydsl_designator(myDsl_designator mydsl_designator) {
        this.mydsl_designator = mydsl_designator;
    }

}