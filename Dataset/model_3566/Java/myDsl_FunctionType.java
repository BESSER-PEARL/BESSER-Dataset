





import java.util.List;
import java.util.ArrayList;

public class myDsl_FunctionType  {

    private String func;





    private myDsl_TypeLit mydsl_typelit;


    public myDsl_FunctionType(
        String func    ) {
        this.func = func;
    }


    public String getFunc() {
        return func;
    }

    public void setFunc(String func) {
        this.func = func;
    }

    public myDsl_TypeLit getMydsl_typelit() {
        return mydsl_typelit;
    }

    public void setMydsl_typelit(myDsl_TypeLit mydsl_typelit) {
        this.mydsl_typelit = mydsl_typelit;
    }

}