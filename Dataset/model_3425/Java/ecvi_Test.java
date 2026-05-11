





import java.util.List;
import java.util.ArrayList;

public class ecvi_Test  {

    private String idref;
    private String testCode;





    private ecvi_Animal ecvi_animal;


    public ecvi_Test(
        String idref,        String testCode    ) {
        this.idref = idref;
        this.testCode = testCode;
    }


    public String getIdref() {
        return idref;
    }

    public void setIdref(String idref) {
        this.idref = idref;
    }
    public String getTestcode() {
        return testCode;
    }

    public void setTestcode(String testCode) {
        this.testCode = testCode;
    }

    public ecvi_Animal getEcvi_animal() {
        return ecvi_animal;
    }

    public void setEcvi_animal(ecvi_Animal ecvi_animal) {
        this.ecvi_animal = ecvi_animal;
    }

}