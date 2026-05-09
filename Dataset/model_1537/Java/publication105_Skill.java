





import java.util.List;
import java.util.ArrayList;

public class publication105_Skill  {

    private String description;





    private publication105_Researcher publication105_researcher;


    public publication105_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public publication105_Researcher getPublication105_researcher() {
        return publication105_researcher;
    }

    public void setPublication105_researcher(publication105_Researcher publication105_researcher) {
        this.publication105_researcher = publication105_researcher;
    }

}