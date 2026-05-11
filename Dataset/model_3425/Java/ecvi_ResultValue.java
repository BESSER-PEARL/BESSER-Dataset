





import java.util.List;
import java.util.ArrayList;

public class ecvi_ResultValue  {

    private String resultFloat;
    private String resultString;
    private String resultName;
    private String resultInteger;





    private ecvi_Test ecvi_test;


    public ecvi_ResultValue(
        String resultFloat,        String resultString,        String resultName,        String resultInteger    ) {
        this.resultFloat = resultFloat;
        this.resultString = resultString;
        this.resultName = resultName;
        this.resultInteger = resultInteger;
    }


    public String getResultfloat() {
        return resultFloat;
    }

    public void setResultfloat(String resultFloat) {
        this.resultFloat = resultFloat;
    }
    public String getResultstring() {
        return resultString;
    }

    public void setResultstring(String resultString) {
        this.resultString = resultString;
    }
    public String getResultname() {
        return resultName;
    }

    public void setResultname(String resultName) {
        this.resultName = resultName;
    }
    public String getResultinteger() {
        return resultInteger;
    }

    public void setResultinteger(String resultInteger) {
        this.resultInteger = resultInteger;
    }

    public ecvi_Test getEcvi_test() {
        return ecvi_test;
    }

    public void setEcvi_test(ecvi_Test ecvi_test) {
        this.ecvi_test = ecvi_test;
    }

}