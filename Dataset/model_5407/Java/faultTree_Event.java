





import java.util.List;
import java.util.ArrayList;

public class faultTree_Event extends FTElement {

    private String title;
    private String description;



    public faultTree_Event(
        String title,        String description    ) {
        super(
        );
        this.title = title;
        this.description = description;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}