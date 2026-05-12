





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_StyleSheetsCollection  {






    private VisioDocument visiodocument;




    private List<StyleSheet> stylesheets;


    public DatadiagramMLXForm_StyleSheetsCollection(
    ) {
        this.stylesheets = new ArrayList<>();
    }

    public DatadiagramMLXForm_StyleSheetsCollection(
        ArrayList<StyleSheet> stylesheets    ) {
        this.stylesheets = stylesheets;
    }


    public VisioDocument getVisiodocument() {
        return visiodocument;
    }

    public void setVisiodocument(VisioDocument visiodocument) {
        this.visiodocument = visiodocument;
    }
    public List<StyleSheet> getStylesheets() {
        return stylesheets;
    }

    public void addStylesheet(Stylesheet stylesheet) {
        this.stylesheets.add(stylesheet);
    }

}