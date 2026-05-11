





import java.util.List;
import java.util.ArrayList;

public class go_FunctionLit extends Literal {






    private go_Signature go_signature;




    private go_FunctionBody go_functionbody;


    public go_FunctionLit(
    ) {
        super(
        );
    }



    public go_Signature getGo_signature() {
        return go_signature;
    }

    public void setGo_signature(go_Signature go_signature) {
        this.go_signature = go_signature;
    }
    public go_FunctionBody getGo_functionbody() {
        return go_functionbody;
    }

    public void setGo_functionbody(go_FunctionBody go_functionbody) {
        this.go_functionbody = go_functionbody;
    }

}