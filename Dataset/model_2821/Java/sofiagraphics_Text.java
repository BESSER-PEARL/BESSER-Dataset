





import java.util.List;
import java.util.ArrayList;

public class sofiagraphics_Text extends Widget {

    private String halign;
    private String valign;
    private String attributeName;
    private String text;



    public sofiagraphics_Text(
        String halign,        String valign,        String attributeName,        String text    ) {
        super(
        );
        this.halign = halign;
        this.valign = valign;
        this.attributeName = attributeName;
        this.text = text;
    }


    public String getHalign() {
        return halign;
    }

    public void setHalign(String halign) {
        this.halign = halign;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getAttributename() {
        return attributeName;
    }

    public void setAttributename(String attributeName) {
        this.attributeName = attributeName;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}