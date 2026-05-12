





import java.util.List;
import java.util.ArrayList;

public class publication102_Skill  {

    private String description;





    private publication102_Researcher publication102_researcher;


    public publication102_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public publication102_Researcher getPublication102_researcher() {
        return publication102_researcher;
    }

    public void setPublication102_researcher(publication102_Researcher publication102_researcher) {
        this.publication102_researcher = publication102_researcher;
    }

}