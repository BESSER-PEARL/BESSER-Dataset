





import java.util.List;
import java.util.ArrayList;

public class XHTML_Map extends Specialpre, I18n, Events {






    private CDATA cdata;




    private Text text;




    private ID id;




    private NMTOKEN nmtoken;




    private StyleSheet stylesheet;


    public XHTML_Map(
    ) {
        super(
        );
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
    public ID getId() {
        return id;
    }

    public void setId(ID id) {
        this.id = id;
    }
    public NMTOKEN getNmtoken() {
        return nmtoken;
    }

    public void setNmtoken(NMTOKEN nmtoken) {
        this.nmtoken = nmtoken;
    }
    public StyleSheet getStylesheet() {
        return stylesheet;
    }

    public void setStylesheet(StyleSheet stylesheet) {
        this.stylesheet = stylesheet;
    }

}