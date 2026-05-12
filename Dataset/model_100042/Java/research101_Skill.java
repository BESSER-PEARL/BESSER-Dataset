





import java.util.List;
import java.util.ArrayList;

public class research101_Skill  {

    private String description;





    private research101_Researcher research101_researcher;


    public research101_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public research101_Researcher getResearch101_researcher() {
        return research101_researcher;
    }

    public void setResearch101_researcher(research101_Researcher research101_researcher) {
        this.research101_researcher = research101_researcher;
    }

}