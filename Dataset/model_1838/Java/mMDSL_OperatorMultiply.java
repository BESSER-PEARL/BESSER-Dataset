





import java.util.List;
import java.util.ArrayList;

public class mMDSL_OperatorMultiply  {

    private String modulo;
    private String multiply;
    private String divide;



    public mMDSL_OperatorMultiply(
        String modulo,        String multiply,        String divide    ) {
        this.modulo = modulo;
        this.multiply = multiply;
        this.divide = divide;
    }


    public String getModulo() {
        return modulo;
    }

    public void setModulo(String modulo) {
        this.modulo = modulo;
    }
    public String getMultiply() {
        return multiply;
    }

    public void setMultiply(String multiply) {
        this.multiply = multiply;
    }
    public String getDivide() {
        return divide;
    }

    public void setDivide(String divide) {
        this.divide = divide;
    }


}