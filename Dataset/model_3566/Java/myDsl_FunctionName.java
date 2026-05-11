





import java.util.List;
import java.util.ArrayList;

public class myDsl_FunctionName  {

    private String id;





    private myDsl_FunctionDecl mydsl_functiondecl;


    public myDsl_FunctionName(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_FunctionDecl getMydsl_functiondecl() {
        return mydsl_functiondecl;
    }

    public void setMydsl_functiondecl(myDsl_FunctionDecl mydsl_functiondecl) {
        this.mydsl_functiondecl = mydsl_functiondecl;
    }

}