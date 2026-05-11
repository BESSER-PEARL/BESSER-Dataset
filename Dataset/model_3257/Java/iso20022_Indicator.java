





import java.util.List;
import java.util.ArrayList;

public class iso20022_Indicator extends Boolean {

    private String meaningWhenTrue;
    private String meaningWhenFalse;



    public iso20022_Indicator(
        String meaningWhenTrue,        String meaningWhenFalse    ) {
        super(
        );
        this.meaningWhenTrue = meaningWhenTrue;
        this.meaningWhenFalse = meaningWhenFalse;
    }


    public String getMeaningwhentrue() {
        return meaningWhenTrue;
    }

    public void setMeaningwhentrue(String meaningWhenTrue) {
        this.meaningWhenTrue = meaningWhenTrue;
    }
    public String getMeaningwhenfalse() {
        return meaningWhenFalse;
    }

    public void setMeaningwhenfalse(String meaningWhenFalse) {
        this.meaningWhenFalse = meaningWhenFalse;
    }


}