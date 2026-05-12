





import java.util.List;
import java.util.ArrayList;

public class research_team_CallForPaper  {

    private String deadline;
    private String category;
    private String title;
    private String url;



    public research_team_CallForPaper(
        String deadline,        String category,        String title,        String url    ) {
        this.deadline = deadline;
        this.category = category;
        this.title = title;
        this.url = url;
    }


    public String getDeadline() {
        return deadline;
    }

    public void setDeadline(String deadline) {
        this.deadline = deadline;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}