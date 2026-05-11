





import java.util.List;
import java.util.ArrayList;

public class go_MethodDecl  {






    private go_FunctionBody go_functionbody;




    private go_MethodName go_methodname;




    private go_Signature go_signature;




    private go_Receiver go_receiver;


    public go_MethodDecl(
    ) {
    }



    public go_FunctionBody getGo_functionbody() {
        return go_functionbody;
    }

    public void setGo_functionbody(go_FunctionBody go_functionbody) {
        this.go_functionbody = go_functionbody;
    }
    public go_MethodName getGo_methodname() {
        return go_methodname;
    }

    public void setGo_methodname(go_MethodName go_methodname) {
        this.go_methodname = go_methodname;
    }
    public go_Signature getGo_signature() {
        return go_signature;
    }

    public void setGo_signature(go_Signature go_signature) {
        this.go_signature = go_signature;
    }
    public go_Receiver getGo_receiver() {
        return go_receiver;
    }

    public void setGo_receiver(go_Receiver go_receiver) {
        this.go_receiver = go_receiver;
    }

}