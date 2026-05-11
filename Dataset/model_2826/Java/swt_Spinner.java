





import java.util.List;
import java.util.ArrayList;

public class swt_Spinner extends IntervalSelector {

    private int textLimit;
    private int digits;



    public swt_Spinner(
        int textLimit,        int digits    ) {
        super(
        );
        this.textLimit = textLimit;
        this.digits = digits;
    }


    public int getTextlimit() {
        return textLimit;
    }

    public void setTextlimit(int textLimit) {
        this.textLimit = textLimit;
    }
    public int getDigits() {
        return digits;
    }

    public void setDigits(int digits) {
        this.digits = digits;
    }


}