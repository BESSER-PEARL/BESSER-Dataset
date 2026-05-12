





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_richstring_RichStringMarkup extends XExpression {

    private String styleClass;
    private String id;





    private richstring_luniferadoc_XExpression richstring_luniferadoc_xexpression;


    public luniferadoc_richstring_RichStringMarkup(
        String styleClass,        String id    ) {
        super(
        );
        this.styleClass = styleClass;
        this.id = id;
    }


    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public richstring_luniferadoc_XExpression getRichstring_luniferadoc_xexpression() {
        return richstring_luniferadoc_xexpression;
    }

    public void setRichstring_luniferadoc_xexpression(richstring_luniferadoc_XExpression richstring_luniferadoc_xexpression) {
        this.richstring_luniferadoc_xexpression = richstring_luniferadoc_xexpression;
    }

}