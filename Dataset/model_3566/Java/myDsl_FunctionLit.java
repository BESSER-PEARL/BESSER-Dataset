





import java.util.List;
import java.util.ArrayList;

public class myDsl_FunctionLit  {

    private String func;





    private myDsl_Literal mydsl_literal;




    private myDsl_FunctionBody mydsl_functionbody;




    private myDsl_Signature mydsl_signature;


    public myDsl_FunctionLit(
        String func    ) {
        this.func = func;
    }


    public String getFunc() {
        return func;
    }

    public void setFunc(String func) {
        this.func = func;
    }

    public myDsl_Literal getMydsl_literal() {
        return mydsl_literal;
    }

    public void setMydsl_literal(myDsl_Literal mydsl_literal) {
        this.mydsl_literal = mydsl_literal;
    }
    public myDsl_FunctionBody getMydsl_functionbody() {
        return mydsl_functionbody;
    }

    public void setMydsl_functionbody(myDsl_FunctionBody mydsl_functionbody) {
        this.mydsl_functionbody = mydsl_functionbody;
    }
    public myDsl_Signature getMydsl_signature() {
        return mydsl_signature;
    }

    public void setMydsl_signature(myDsl_Signature mydsl_signature) {
        this.mydsl_signature = mydsl_signature;
    }

}