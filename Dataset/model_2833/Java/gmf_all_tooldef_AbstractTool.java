





import java.util.List;
import java.util.ArrayList;

public class gmf_all_tooldef_AbstractTool  {

    private String description;
    private String title;



    public gmf_all_tooldef_AbstractTool(
        String description,        String title    ) {
        this.description = description;
        this.title = title;
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


}