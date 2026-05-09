





import java.util.List;
import java.util.ArrayList;

public class researchvc_Skill  {

    private String description;





    private researchvc_Researcher researchvc_researcher;


    public researchvc_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public researchvc_Researcher getResearchvc_researcher() {
        return researchvc_researcher;
    }

    public void setResearchvc_researcher(researchvc_Researcher researchvc_researcher) {
        this.researchvc_researcher = researchvc_researcher;
    }

}