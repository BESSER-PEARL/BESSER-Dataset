





import java.util.List;
import java.util.ArrayList;

public class lobj_SimpleDidacMeta  {

    private String description;
    private String title;
    private String keywords;
    private String id;





    private lobj_BlockMeta lobj_blockmeta;




    private lobj_Theme lobj_theme;




    private lobj_Language lobj_language;


    public lobj_SimpleDidacMeta(
        String description,        String title,        String keywords,        String id    ) {
        this.description = description;
        this.title = title;
        this.keywords = keywords;
        this.id = id;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public lobj_BlockMeta getLobj_blockmeta() {
        return lobj_blockmeta;
    }

    public void setLobj_blockmeta(lobj_BlockMeta lobj_blockmeta) {
        this.lobj_blockmeta = lobj_blockmeta;
    }
    public lobj_Theme getLobj_theme() {
        return lobj_theme;
    }

    public void setLobj_theme(lobj_Theme lobj_theme) {
        this.lobj_theme = lobj_theme;
    }
    public lobj_Language getLobj_language() {
        return lobj_language;
    }

    public void setLobj_language(lobj_Language lobj_language) {
        this.lobj_language = lobj_language;
    }

}