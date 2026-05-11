





import java.util.List;
import java.util.ArrayList;

public class go_FunctionDecl  {






    private go_FunctionBody go_functionbody;




    private go_Signature go_signature;




    private go_FunctionName go_functionname;


    public go_FunctionDecl(
    ) {
    }



    public go_FunctionBody getGo_functionbody() {
        return go_functionbody;
    }

    public void setGo_functionbody(go_FunctionBody go_functionbody) {
        this.go_functionbody = go_functionbody;
    }
    public go_Signature getGo_signature() {
        return go_signature;
    }

    public void setGo_signature(go_Signature go_signature) {
        this.go_signature = go_signature;
    }
    public go_FunctionName getGo_functionname() {
        return go_functionname;
    }

    public void setGo_functionname(go_FunctionName go_functionname) {
        this.go_functionname = go_functionname;
    }

}