





import java.util.List;
import java.util.ArrayList;

public class Interpreter_ByteCode_BOP  {

    private String binaryOp;



    public Interpreter_ByteCode_BOP(
        String binaryOp    ) {
        this.binaryOp = binaryOp;
    }


    public String getBinaryop() {
        return binaryOp;
    }

    public void setBinaryop(String binaryOp) {
        this.binaryOp = binaryOp;
    }


}