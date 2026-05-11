





import java.util.List;
import java.util.ArrayList;

public class myDsl_FunctionBody  {






    private myDsl_Block mydsl_block;




    private myDsl_FunctionDecl mydsl_functiondecl;




    private myDsl_MethodDecl mydsl_methoddecl;


    public myDsl_FunctionBody(
    ) {
    }



    public myDsl_Block getMydsl_block() {
        return mydsl_block;
    }

    public void setMydsl_block(myDsl_Block mydsl_block) {
        this.mydsl_block = mydsl_block;
    }
    public myDsl_FunctionDecl getMydsl_functiondecl() {
        return mydsl_functiondecl;
    }

    public void setMydsl_functiondecl(myDsl_FunctionDecl mydsl_functiondecl) {
        this.mydsl_functiondecl = mydsl_functiondecl;
    }
    public myDsl_MethodDecl getMydsl_methoddecl() {
        return mydsl_methoddecl;
    }

    public void setMydsl_methoddecl(myDsl_MethodDecl mydsl_methoddecl) {
        this.mydsl_methoddecl = mydsl_methoddecl;
    }

}