





import java.util.List;
import java.util.ArrayList;

public class research_Skill  {

    private String description;





    private research_Researcher research_researcher;


    public research_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public research_Researcher getResearch_researcher() {
        return research_researcher;
    }

    public void setResearch_researcher(research_Researcher research_researcher) {
        this.research_researcher = research_researcher;
    }

}