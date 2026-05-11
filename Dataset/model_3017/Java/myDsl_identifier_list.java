





import java.util.List;
import java.util.ArrayList;

public class myDsl_identifier_list  {

    private String identifier;





    private myDsl_direct_declarator2 mydsl_direct_declarator2;


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

    public myDsl_direct_declarator2 getMydsl_direct_declarator2() {
        return mydsl_direct_declarator2;
    }

    public void setMydsl_direct_declarator2(myDsl_direct_declarator2 mydsl_direct_declarator2) {
        this.mydsl_direct_declarator2 = mydsl_direct_declarator2;
    }

}