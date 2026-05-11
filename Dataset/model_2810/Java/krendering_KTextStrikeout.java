





import java.util.List;
import java.util.ArrayList;

public class krendering_KTextStrikeout extends KStyle {

    private String struckOut;



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


}