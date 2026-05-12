





import java.util.List;
import java.util.ArrayList;

public class research_team_Team  {

    private String name;
    private String status;
    private String meaning;
    private String urlPage;



    public research_team_Team(
        String name,        String status,        String meaning,        String urlPage    ) {
        this.name = name;
        this.status = status;
        this.meaning = meaning;
        this.urlPage = urlPage;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getMeaning() {
        return meaning;
    }

    public void setMeaning(String meaning) {
        this.meaning = meaning;
    }
    public String getUrlpage() {
        return urlPage;
    }

    public void setUrlpage(String urlPage) {
        this.urlPage = urlPage;
    }


}