





import java.util.List;
import java.util.ArrayList;

public class research13_Skill  {

    private String description;





    private research13_Researcher research13_researcher;


    public research13_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public research13_Researcher getResearch13_researcher() {
        return research13_researcher;
    }

    public void setResearch13_researcher(research13_Researcher research13_researcher) {
        this.research13_researcher = research13_researcher;
    }

}