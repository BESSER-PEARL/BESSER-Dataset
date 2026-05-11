





import java.util.List;
import java.util.ArrayList;

public class model_Discussion  {

    private String discussions;





    private model_Content model_content;


    public model_Discussion(
        String discussions    ) {
        this.discussions = discussions;
    }


    public String getDiscussions() {
        return discussions;
    }

    public void setDiscussions(String discussions) {
        this.discussions = discussions;
    }

    public model_Content getModel_content() {
        return model_content;
    }

    public void setModel_content(model_Content model_content) {
        this.model_content = model_content;
    }

}