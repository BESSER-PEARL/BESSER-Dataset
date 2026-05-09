





import java.util.List;
import java.util.ArrayList;

public class shr5_BerechneteAttribute  {

    private int menschenkenntnis;
    private int errinerungsvermoegen;
    private int selbstbeherrschung;



    public shr5_BerechneteAttribute(
        int menschenkenntnis,        int errinerungsvermoegen,        int selbstbeherrschung    ) {
        this.menschenkenntnis = menschenkenntnis;
        this.errinerungsvermoegen = errinerungsvermoegen;
        this.selbstbeherrschung = selbstbeherrschung;
    }


    public int getMenschenkenntnis() {
        return menschenkenntnis;
    }

    public void setMenschenkenntnis(int menschenkenntnis) {
        this.menschenkenntnis = menschenkenntnis;
    }
    public int getErrinerungsvermoegen() {
        return errinerungsvermoegen;
    }

    public void setErrinerungsvermoegen(int errinerungsvermoegen) {
        this.errinerungsvermoegen = errinerungsvermoegen;
    }
    public int getSelbstbeherrschung() {
        return selbstbeherrschung;
    }

    public void setSelbstbeherrschung(int selbstbeherrschung) {
        this.selbstbeherrschung = selbstbeherrschung;
    }


}