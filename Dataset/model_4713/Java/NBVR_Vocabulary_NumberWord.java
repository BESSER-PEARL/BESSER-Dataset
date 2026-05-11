





import java.util.List;
import java.util.ArrayList;

public class NBVR_Vocabulary_NumberWord extends Word {

    private boolean decimal;
    private int value;



    public NBVR_Vocabulary_NumberWord(
        boolean decimal,        int value    ) {
        super(
        );
        this.decimal = decimal;
        this.value = value;
    }


    public boolean getDecimal() {
        return decimal;
    }

    public void setDecimal(boolean decimal) {
        this.decimal = decimal;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}