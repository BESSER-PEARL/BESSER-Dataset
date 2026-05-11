





import java.util.List;
import java.util.ArrayList;

public class lobj_Coursetype  {

    private String id;
    private String description;
    private String title;





    private lobj_Language lobj_language;




    private lobj_Course lobj_course;


    public lobj_Coursetype(
        String id,        String description,        String title    ) {
        this.id = id;
        this.description = description;
        this.title = title;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
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

    public lobj_Language getLobj_language() {
        return lobj_language;
    }

    public void setLobj_language(lobj_Language lobj_language) {
        this.lobj_language = lobj_language;
    }
    public lobj_Course getLobj_course() {
        return lobj_course;
    }

    public void setLobj_course(lobj_Course lobj_course) {
        this.lobj_course = lobj_course;
    }

}