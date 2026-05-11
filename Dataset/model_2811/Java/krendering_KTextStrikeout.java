





import java.util.List;
import java.util.ArrayList;

public class krendering_KTextStrikeout extends KStyle {

    private String struckOut;





    private krendering_KColor krendering_kcolor;


    public krendering_KTextStrikeout(
        String struckOut    ) {
        super(
        );
        this.struckOut = struckOut;
    }


    public String getStruckout() {
        return struckOut;
    }

    public void setStruckout(String struckOut) {
        this.struckOut = struckOut;
    }

    public krendering_KColor getKrendering_kcolor() {
        return krendering_kcolor;
    }

    public void setKrendering_kcolor(krendering_KColor krendering_kcolor) {
        this.krendering_kcolor = krendering_kcolor;
    }

}