





import java.util.List;
import java.util.ArrayList;

public class ansic_identifier_list  {

    private String identifier;





    private ansic_direct_declarator_complemento ansic_direct_declarator_complemento;


    public ansic_identifier_list(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public ansic_direct_declarator_complemento getAnsic_direct_declarator_complemento() {
        return ansic_direct_declarator_complemento;
    }

    public void setAnsic_direct_declarator_complemento(ansic_direct_declarator_complemento ansic_direct_declarator_complemento) {
        this.ansic_direct_declarator_complemento = ansic_direct_declarator_complemento;
    }

}