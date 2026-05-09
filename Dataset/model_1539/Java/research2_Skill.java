





import java.util.List;
import java.util.ArrayList;

public class research2_Skill  {

    private String description;





    private research2_Researcher research2_researcher;


    public research2_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public research2_Researcher getResearch2_researcher() {
        return research2_researcher;
    }

    public void setResearch2_researcher(research2_Researcher research2_researcher) {
        this.research2_researcher = research2_researcher;
    }

}