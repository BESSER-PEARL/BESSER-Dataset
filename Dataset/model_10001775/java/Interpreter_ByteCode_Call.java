





import java.util.List;
import java.util.ArrayList;

public class Interpreter_ByteCode_Call  {

    private String funcname;
    private int address;



    public Interpreter_ByteCode_Call(
        String funcname,        int address    ) {
        this.funcname = funcname;
        this.address = address;
    }


    public String getFuncname() {
        return funcname;
    }

    public void setFuncname(String funcname) {
        this.funcname = funcname;
    }
    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }


}