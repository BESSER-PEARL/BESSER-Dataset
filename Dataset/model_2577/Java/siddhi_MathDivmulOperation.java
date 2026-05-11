





import java.util.List;
import java.util.ArrayList;

public class siddhi_MathDivmulOperation extends MathAddsubOperation {

    private String devide;
    private String mod;
    private String multiply;





    private siddhi_MathAddsubOperation siddhi_mathaddsuboperation;


    public siddhi_MathDivmulOperation(
        String devide,        String mod,        String multiply    ) {
        super(
        );
        this.devide = devide;
        this.mod = mod;
        this.multiply = multiply;
    }


    public String getDevide() {
        return devide;
    }

    public void setDevide(String devide) {
        this.devide = devide;
    }
    public String getMod() {
        return mod;
    }

    public void setMod(String mod) {
        this.mod = mod;
    }
    public String getMultiply() {
        return multiply;
    }

    public void setMultiply(String multiply) {
        this.multiply = multiply;
    }

    public siddhi_MathAddsubOperation getSiddhi_mathaddsuboperation() {
        return siddhi_mathaddsuboperation;
    }

    public void setSiddhi_mathaddsuboperation(siddhi_MathAddsubOperation siddhi_mathaddsuboperation) {
        this.siddhi_mathaddsuboperation = siddhi_mathaddsuboperation;
    }

}