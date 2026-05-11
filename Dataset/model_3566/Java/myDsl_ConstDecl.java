





import java.util.List;
import java.util.ArrayList;

public class myDsl_ConstDecl  {

    private String const;





    private myDsl_Declaration mydsl_declaration;


    public myDsl_ConstDecl(
        String const    ) {
        this.const = const;
    }


    public String getConst() {
        return const;
    }

    public void setConst(String const) {
        this.const = const;
    }

    public myDsl_Declaration getMydsl_declaration() {
        return mydsl_declaration;
    }

    public void setMydsl_declaration(myDsl_Declaration mydsl_declaration) {
        this.mydsl_declaration = mydsl_declaration;
    }

}