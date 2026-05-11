





import java.util.List;
import java.util.ArrayList;

public class krendering_KTextUnderline extends KStyle {

    private String underline;





    private krendering_KColor krendering_kcolor;


    public krendering_KTextUnderline(
        String underline    ) {
        super(
        );
        this.underline = underline;
    }


    public String getUnderline() {
        return underline;
    }

    public void setUnderline(String underline) {
        this.underline = underline;
    }

    public krendering_KColor getKrendering_kcolor() {
        return krendering_kcolor;
    }

    public void setKrendering_kcolor(krendering_KColor krendering_kcolor) {
        this.krendering_kcolor = krendering_kcolor;
    }

}