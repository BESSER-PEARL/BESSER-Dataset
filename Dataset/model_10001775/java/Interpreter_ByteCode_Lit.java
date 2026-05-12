





import java.util.List;
import java.util.ArrayList;

public class Interpreter_ByteCode_Lit  {

    private int value;
    private String var;



    public Interpreter_ByteCode_Lit(
        int value,        String var    ) {
        this.value = value;
        this.var = var;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }


}