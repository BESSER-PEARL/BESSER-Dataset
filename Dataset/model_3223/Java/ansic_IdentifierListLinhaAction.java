





import java.util.List;
import java.util.ArrayList;

public class ansic_IdentifierListLinhaAction extends identifier_list_linha {

    private String identifier;





    private ansic_identifier_list_linha ansic_identifier_list_linha;


    public ansic_IdentifierListLinhaAction(
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

    public ansic_identifier_list_linha getAnsic_identifier_list_linha() {
        return ansic_identifier_list_linha;
    }

    public void setAnsic_identifier_list_linha(ansic_identifier_list_linha ansic_identifier_list_linha) {
        this.ansic_identifier_list_linha = ansic_identifier_list_linha;
    }

}