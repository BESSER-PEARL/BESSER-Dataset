





import java.util.List;
import java.util.ArrayList;

public class lobj_TitleMeta  {

    private String title;
    private String id;





    private lobj_Language lobj_language;




    private lobj_Category lobj_category;


    public lobj_TitleMeta(
        String title,        String id    ) {
        this.title = title;
        this.id = id;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public lobj_Language getLobj_language() {
        return lobj_language;
    }

    public void setLobj_language(lobj_Language lobj_language) {
        this.lobj_language = lobj_language;
    }
    public lobj_Category getLobj_category() {
        return lobj_category;
    }

    public void setLobj_category(lobj_Category lobj_category) {
        this.lobj_category = lobj_category;
    }

}