





import java.util.List;
import java.util.ArrayList;

public class tp6_Skill  {

    private String description;





    private tp6_Researcher tp6_researcher;


    public tp6_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public tp6_Researcher getTp6_researcher() {
        return tp6_researcher;
    }

    public void setTp6_researcher(tp6_Researcher tp6_researcher) {
        this.tp6_researcher = tp6_researcher;
    }

}