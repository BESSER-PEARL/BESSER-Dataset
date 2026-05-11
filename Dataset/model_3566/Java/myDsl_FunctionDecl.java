





import java.util.List;
import java.util.ArrayList;

public class myDsl_FunctionDecl  {






    private myDsl_Signature mydsl_signature;




    private myDsl_TopLevelDecl mydsl_topleveldecl;


    public myDsl_FunctionDecl(
    ) {
    }



    public myDsl_Signature getMydsl_signature() {
        return mydsl_signature;
    }

    public void setMydsl_signature(myDsl_Signature mydsl_signature) {
        this.mydsl_signature = mydsl_signature;
    }
    public myDsl_TopLevelDecl getMydsl_topleveldecl() {
        return mydsl_topleveldecl;
    }

    public void setMydsl_topleveldecl(myDsl_TopLevelDecl mydsl_topleveldecl) {
        this.mydsl_topleveldecl = mydsl_topleveldecl;
    }

}