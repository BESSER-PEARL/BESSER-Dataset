





import java.util.List;
import java.util.ArrayList;

public class myDsl_Tag  {

    private String string_lit;





    private myDsl_FieldDecl mydsl_fielddecl;


    public myDsl_Tag(
        String string_lit    ) {
        this.string_lit = string_lit;
    }


    public String getString_lit() {
        return string_lit;
    }

    public void setString_lit(String string_lit) {
        this.string_lit = string_lit;
    }

    public myDsl_FieldDecl getMydsl_fielddecl() {
        return mydsl_fielddecl;
    }

    public void setMydsl_fielddecl(myDsl_FieldDecl mydsl_fielddecl) {
        this.mydsl_fielddecl = mydsl_fielddecl;
    }

}