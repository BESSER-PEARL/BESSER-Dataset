





import java.util.List;
import java.util.ArrayList;

public class research_Position extends Named {

    private String description;





    private research_Researcher research_researcher;




    private research_PublicationSystem research_publicationsystem;




    private research_Position research_position;


    public research_Position(
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

    public research_Researcher getResearch_researcher() {
        return research_researcher;
    }

    public void setResearch_researcher(research_Researcher research_researcher) {
        this.research_researcher = research_researcher;
    }
    public research_PublicationSystem getResearch_publicationsystem() {
        return research_publicationsystem;
    }

    public void setResearch_publicationsystem(research_PublicationSystem research_publicationsystem) {
        this.research_publicationsystem = research_publicationsystem;
    }
    public research_Position getResearch_position() {
        return research_position;
    }

    public void setResearch_position(research_Position research_position) {
        this.research_position = research_position;
    }

}