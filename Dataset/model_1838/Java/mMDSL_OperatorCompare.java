





import java.util.List;
import java.util.ArrayList;

public class mMDSL_OperatorCompare  {

    private String greaterequal;
    private String greater;
    private String lesserequal;
    private String lesser;



    public mMDSL_OperatorCompare(
        String greaterequal,        String greater,        String lesserequal,        String lesser    ) {
        this.greaterequal = greaterequal;
        this.greater = greater;
        this.lesserequal = lesserequal;
        this.lesser = lesser;
    }


    public String getGreaterequal() {
        return greaterequal;
    }

    public void setGreaterequal(String greaterequal) {
        this.greaterequal = greaterequal;
    }
    public String getGreater() {
        return greater;
    }

    public void setGreater(String greater) {
        this.greater = greater;
    }
    public String getLesserequal() {
        return lesserequal;
    }

    public void setLesserequal(String lesserequal) {
        this.lesserequal = lesserequal;
    }
    public String getLesser() {
        return lesser;
    }

    public void setLesser(String lesser) {
        this.lesser = lesser;
    }


}