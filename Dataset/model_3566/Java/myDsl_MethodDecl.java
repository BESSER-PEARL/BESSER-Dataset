





import java.util.List;
import java.util.ArrayList;

public class myDsl_MethodDecl  {






    private myDsl_MethodName mydsl_methodname;




    private myDsl_Signature mydsl_signature;




    private myDsl_TopLevelDecl mydsl_topleveldecl;


    public myDsl_MethodDecl(
    ) {
    }



    public myDsl_MethodName getMydsl_methodname() {
        return mydsl_methodname;
    }

    public void setMydsl_methodname(myDsl_MethodName mydsl_methodname) {
        this.mydsl_methodname = mydsl_methodname;
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