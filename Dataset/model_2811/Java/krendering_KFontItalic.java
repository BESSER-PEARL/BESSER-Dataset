





import java.util.List;
import java.util.ArrayList;

public class krendering_KFontItalic extends KStyle {

    private boolean italic;



    public krendering_KFontItalic(
        boolean italic    ) {
        super(
        );
        this.italic = italic;
    }


    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
    }


}