





import java.util.List;
import java.util.ArrayList;

public class publication103_Skill  {

    private String description;





    private publication103_Researcher publication103_researcher;


    public publication103_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public publication103_Researcher getPublication103_researcher() {
        return publication103_researcher;
    }

    public void setPublication103_researcher(publication103_Researcher publication103_researcher) {
        this.publication103_researcher = publication103_researcher;
    }

}