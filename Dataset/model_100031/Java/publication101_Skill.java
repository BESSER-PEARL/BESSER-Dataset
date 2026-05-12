





import java.util.List;
import java.util.ArrayList;

public class publication101_Skill  {

    private String description;





    private publication101_Researcher publication101_researcher;


    public publication101_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public publication101_Researcher getPublication101_researcher() {
        return publication101_researcher;
    }

    public void setPublication101_researcher(publication101_Researcher publication101_researcher) {
        this.publication101_researcher = publication101_researcher;
    }

}