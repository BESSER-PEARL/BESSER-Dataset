





import java.util.List;
import java.util.ArrayList;

public class myDsl_IdentifierListLinhaAction extends identifier_list_linha {

    private String identifier;





    private myDsl_identifier_list_linha mydsl_identifier_list_linha;


    public myDsl_IdentifierListLinhaAction(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public myDsl_identifier_list_linha getMydsl_identifier_list_linha() {
        return mydsl_identifier_list_linha;
    }

    public void setMydsl_identifier_list_linha(myDsl_identifier_list_linha mydsl_identifier_list_linha) {
        this.mydsl_identifier_list_linha = mydsl_identifier_list_linha;
    }

}