





import java.util.List;
import java.util.ArrayList;

public class conference_Talk  {

    private String title;
    private String documentation;
    private String type;



    public conference_Talk(
        String title,        String documentation,        String type    ) {
        this.title = title;
        this.documentation = documentation;
        this.type = type;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}