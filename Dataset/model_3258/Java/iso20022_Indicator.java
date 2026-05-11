





import java.util.List;
import java.util.ArrayList;

public class iso20022_Indicator extends Boolean {

    private String meaningWhenFalse;
    private String meaningWhenTrue;



    public iso20022_Indicator(
        String meaningWhenFalse,        String meaningWhenTrue    ) {
        super(
        );
        this.meaningWhenFalse = meaningWhenFalse;
        this.meaningWhenTrue = meaningWhenTrue;
    }


    public String getMeaningwhenfalse() {
        return meaningWhenFalse;
    }

    public void setMeaningwhenfalse(String meaningWhenFalse) {
        this.meaningWhenFalse = meaningWhenFalse;
    }
    public String getMeaningwhentrue() {
        return meaningWhenTrue;
    }

    public void setMeaningwhentrue(String meaningWhenTrue) {
        this.meaningWhenTrue = meaningWhenTrue;
    }


}