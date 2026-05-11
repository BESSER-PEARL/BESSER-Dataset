





import java.util.List;
import java.util.ArrayList;

public class myDsl_ImportDecl  {

    private String importt;





    private myDsl_SourceFile mydsl_sourcefile;


    public myDsl_ImportDecl(
        String importt    ) {
        this.importt = importt;
    }


    public String getImportt() {
        return importt;
    }

    public void setImportt(String importt) {
        this.importt = importt;
    }

    public myDsl_SourceFile getMydsl_sourcefile() {
        return mydsl_sourcefile;
    }

    public void setMydsl_sourcefile(myDsl_SourceFile mydsl_sourcefile) {
        this.mydsl_sourcefile = mydsl_sourcefile;
    }

}