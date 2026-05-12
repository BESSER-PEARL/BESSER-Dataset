





import java.util.List;
import java.util.ArrayList;

public class research20_Skill  {

    private String description;





    private research20_Researcher research20_researcher;


    public research20_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public research20_Researcher getResearch20_researcher() {
        return research20_researcher;
    }

    public void setResearch20_researcher(research20_Researcher research20_researcher) {
        this.research20_researcher = research20_researcher;
    }

}