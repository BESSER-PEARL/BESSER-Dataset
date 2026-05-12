





import java.util.List;
import java.util.ArrayList;

public class XHTML_Button extends Focus, Attrs, Inlineforms {

    private String disabled;
    private String type;





    private List<ButtonContent> buttoncontents;




    private CDATA cdata;




    private CDATA cdata;


    public XHTML_Button(
        String disabled,        String type    ) {
        super(
        );
        this.disabled = disabled;
        this.type = type;
        this.buttoncontents = new ArrayList<>();
    }

    public XHTML_Button(
        String disabled,        String type        ArrayList<ButtonContent> buttoncontents    ) {
        this.disabled = disabled;
        this.type = type;
        this.buttoncontents = buttoncontents;
    }

    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<ButtonContent> getButtoncontents() {
        return buttoncontents;
    }

    public void addButtoncontent(Buttoncontent buttoncontent) {
        this.buttoncontents.add(buttoncontent);
    }
    public CDATA getCdata() {
        return cdata;
    }

    public void setCdata(CDATA cdata) {
        this.cdata = cdata;
    }
    public CDATA getCdata() {
        return cdata;
    }

    public void setCdata(CDATA cdata) {
        this.cdata = cdata;
    }

}