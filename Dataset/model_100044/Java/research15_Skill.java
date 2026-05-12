





import java.util.List;
import java.util.ArrayList;

public class research15_Skill  {

    private String description;





    private research15_Researcher research15_researcher;


    public research15_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public research15_Researcher getResearch15_researcher() {
        return research15_researcher;
    }

    public void setResearch15_researcher(research15_Researcher research15_researcher) {
        this.research15_researcher = research15_researcher;
    }

}