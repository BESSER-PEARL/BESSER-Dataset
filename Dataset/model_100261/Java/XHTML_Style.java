





import java.util.List;
import java.util.ArrayList;

public class XHTML_Style extends PCDATA, HeadMisc {

    private String xml_space;





    private ContentType contenttype;




    private Text text;




    private ID id;




    private I18n i18n;


    public XHTML_Style(
        String xml_space    ) {
        super(
        );
        this.xml_space = xml_space;
    }


    public String getXml_space() {
        return xml_space;
    }

    public void setXml_space(String xml_space) {
        this.xml_space = xml_space;
    }

    public ContentType getContenttype() {
        return contenttype;
    }

    public void setContenttype(ContentType contenttype) {
        this.contenttype = contenttype;
    }
    public Text getText() {
        return text;
    }

    public void setText(Text text) {
        this.text = text;
    }
    public ID getId() {
        return id;
    }

    public void setId(ID id) {
        this.id = id;
    }
    public I18n getI18n() {
        return i18n;
    }

    public void setI18n(I18n i18n) {
        this.i18n = i18n;
    }

}