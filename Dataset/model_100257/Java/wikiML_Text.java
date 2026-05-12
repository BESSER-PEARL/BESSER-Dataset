





import java.util.List;
import java.util.ArrayList;

public class wikiML_Text extends AbstractUnformattedInlineContent {

    private String name;





    private wikiML_Category wikiml_category;


    public wikiML_Text(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public wikiML_Category getWikiml_category() {
        return wikiml_category;
    }

    public void setWikiml_category(wikiML_Category wikiml_category) {
        this.wikiml_category = wikiml_category;
    }

}