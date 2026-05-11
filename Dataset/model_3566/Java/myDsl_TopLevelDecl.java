





import java.util.List;
import java.util.ArrayList;

public class myDsl_TopLevelDecl  {






    private myDsl_Declaration mydsl_declaration;




    private myDsl_SourceFile mydsl_sourcefile;


    public myDsl_TopLevelDecl(
    ) {
    }



    public myDsl_Declaration getMydsl_declaration() {
        return mydsl_declaration;
    }

    public void setMydsl_declaration(myDsl_Declaration mydsl_declaration) {
        this.mydsl_declaration = mydsl_declaration;
    }
    public myDsl_SourceFile getMydsl_sourcefile() {
        return mydsl_sourcefile;
    }

    public void setMydsl_sourcefile(myDsl_SourceFile mydsl_sourcefile) {
        this.mydsl_sourcefile = mydsl_sourcefile;
    }

}