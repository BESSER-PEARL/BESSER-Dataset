





import java.util.List;
import java.util.ArrayList;

public class XHTML_Option extends SelectElement, PCDATA, Attrs {

    private String disabled;
    private String selected;





    private CDATA cdata;




    private Text text;


    public XHTML_Option(
        String disabled,        String selected    ) {
        super(
        );
        this.disabled = disabled;
        this.selected = selected;
    }


    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }
    public String getSelected() {
        return selected;
    }

    public void setSelected(String selected) {
        this.selected = selected;
    }

    public CDATA getCdata() {
        return cdata;
    }

    public void setCdata(CDATA cdata) {
        this.cdata = cdata;
    }
    public Text getText() {
        return text;
    }

    public void setText(Text text) {
        this.text = text;
    }

}