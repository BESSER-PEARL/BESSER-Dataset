





import java.util.List;
import java.util.ArrayList;

public class research19_Position extends Named {

    private String description;





    private research19_PublicationSystem research19_publicationsystem;




    private research19_Position research19_position;




    private research19_Researcher research19_researcher;


    public research19_Position(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public research19_PublicationSystem getResearch19_publicationsystem() {
        return research19_publicationsystem;
    }

    public void setResearch19_publicationsystem(research19_PublicationSystem research19_publicationsystem) {
        this.research19_publicationsystem = research19_publicationsystem;
    }
    public research19_Position getResearch19_position() {
        return research19_position;
    }

    public void setResearch19_position(research19_Position research19_position) {
        this.research19_position = research19_position;
    }
    public research19_Researcher getResearch19_researcher() {
        return research19_researcher;
    }

    public void setResearch19_researcher(research19_Researcher research19_researcher) {
        this.research19_researcher = research19_researcher;
    }

}