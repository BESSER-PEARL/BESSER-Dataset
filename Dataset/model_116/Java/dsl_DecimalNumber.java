





import java.util.List;
import java.util.ArrayList;

public class dsl_DecimalNumber  {

    private String decDigitsUnderscore;
    private int decDigits;



    public dsl_DecimalNumber(
        String decDigitsUnderscore,        int decDigits    ) {
        this.decDigitsUnderscore = decDigitsUnderscore;
        this.decDigits = decDigits;
    }


    public String getDecdigitsunderscore() {
        return decDigitsUnderscore;
    }

    public void setDecdigitsunderscore(String decDigitsUnderscore) {
        this.decDigitsUnderscore = decDigitsUnderscore;
    }
    public int getDecdigits() {
        return decDigits;
    }

    public void setDecdigits(int decDigits) {
        this.decDigits = decDigits;
    }


}