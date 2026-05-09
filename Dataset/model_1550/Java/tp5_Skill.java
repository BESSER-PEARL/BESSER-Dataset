





import java.util.List;
import java.util.ArrayList;

public class tp5_Skill  {

    private String description;





    private tp5_Researcher tp5_researcher;


    public tp5_Skill(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public tp5_Researcher getTp5_researcher() {
        return tp5_researcher;
    }

    public void setTp5_researcher(tp5_Researcher tp5_researcher) {
        this.tp5_researcher = tp5_researcher;
    }

}