





import java.util.List;
import java.util.ArrayList;

public class myDsl_identifier_list  {

    private String identifier;





    private myDsl_direct_declarator_complemento mydsl_direct_declarator_complemento;


    public myDsl_identifier_list(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public myDsl_direct_declarator_complemento getMydsl_direct_declarator_complemento() {
        return mydsl_direct_declarator_complemento;
    }

    public void setMydsl_direct_declarator_complemento(myDsl_direct_declarator_complemento mydsl_direct_declarator_complemento) {
        this.mydsl_direct_declarator_complemento = mydsl_direct_declarator_complemento;
    }

}