





import java.util.List;
import java.util.ArrayList;

public class xwiki_Translations extends LinkCollection {

    private String default;





    private List<xwiki_Translation> xwiki_translations;




    private xwiki_PageSummary xwiki_pagesummary;


    public xwiki_Translations(
        String default    ) {
        super(
        );
        this.default = default;
        this.xwiki_translations = new ArrayList<>();
    }

    public xwiki_Translations(
        String default        ArrayList<xwiki_Translation> xwiki_translations    ) {
        this.default = default;
        this.xwiki_translations = xwiki_translations;
    }

    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public List<xwiki_Translation> getXwiki_translations() {
        return xwiki_translations;
    }

    public void addXwiki_translation(Xwiki_translation xwiki_translation) {
        this.xwiki_translations.add(xwiki_translation);
    }
    public xwiki_PageSummary getXwiki_pagesummary() {
        return xwiki_pagesummary;
    }

    public void setXwiki_pagesummary(xwiki_PageSummary xwiki_pagesummary) {
        this.xwiki_pagesummary = xwiki_pagesummary;
    }

}