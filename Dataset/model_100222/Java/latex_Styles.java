





import java.util.List;
import java.util.ArrayList;

public class latex_Styles  {

    private String stylesnames;
    private String stylenames;
    private String styleprefix;



    public latex_Styles(
        String stylesnames,        String stylenames,        String styleprefix    ) {
        this.stylesnames = stylesnames;
        this.stylenames = stylenames;
        this.styleprefix = styleprefix;
    }


    public String getStylesnames() {
        return stylesnames;
    }

    public void setStylesnames(String stylesnames) {
        this.stylesnames = stylesnames;
    }
    public String getStylenames() {
        return stylenames;
    }

    public void setStylenames(String stylenames) {
        this.stylenames = stylenames;
    }
    public String getStyleprefix() {
        return styleprefix;
    }

    public void setStyleprefix(String styleprefix) {
        this.styleprefix = styleprefix;
    }


}