





import java.util.List;
import java.util.ArrayList;

public class py_ExprSimple  {

    private String str;
    private String sym;
    private String varSimple;



    public py_ExprSimple(
        String str,        String sym,        String varSimple    ) {
        this.str = str;
        this.sym = sym;
        this.varSimple = varSimple;
    }


    public String getStr() {
        return str;
    }

    public void setStr(String str) {
        this.str = str;
    }
    public String getSym() {
        return sym;
    }

    public void setSym(String sym) {
        this.sym = sym;
    }
    public String getVarsimple() {
        return varSimple;
    }

    public void setVarsimple(String varSimple) {
        this.varSimple = varSimple;
    }


}