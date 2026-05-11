





import java.util.List;
import java.util.ArrayList;

public class myDsl_TypeDecl  {

    private String typekeyword;





    private myDsl_Declaration mydsl_declaration;


    public myDsl_TypeDecl(
        String typekeyword    ) {
        this.typekeyword = typekeyword;
    }


    public String getTypekeyword() {
        return typekeyword;
    }

    public void setTypekeyword(String typekeyword) {
        this.typekeyword = typekeyword;
    }

    public myDsl_Declaration getMydsl_declaration() {
        return mydsl_declaration;
    }

    public void setMydsl_declaration(myDsl_Declaration mydsl_declaration) {
        this.mydsl_declaration = mydsl_declaration;
    }

}