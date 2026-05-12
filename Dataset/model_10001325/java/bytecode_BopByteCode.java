





import java.util.List;
import java.util.ArrayList;

public class bytecode_BopByteCode  {

    private String theOperator;
    private String byteCode;



    public bytecode_BopByteCode(
        String theOperator,        String byteCode    ) {
        this.theOperator = theOperator;
        this.byteCode = byteCode;
    }


    public String getTheoperator() {
        return theOperator;
    }

    public void setTheoperator(String theOperator) {
        this.theOperator = theOperator;
    }
    public String getBytecode() {
        return byteCode;
    }

    public void setBytecode(String byteCode) {
        this.byteCode = byteCode;
    }


}