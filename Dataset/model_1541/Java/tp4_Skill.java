





import java.util.List;
import java.util.ArrayList;

public class tp4_Skill  {

    private String description;





    private tp4_Researcher tp4_researcher;


    public tp4_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public tp4_Researcher getTp4_researcher() {
        return tp4_researcher;
    }

    public void setTp4_researcher(tp4_Researcher tp4_researcher) {
        this.tp4_researcher = tp4_researcher;
    }

}