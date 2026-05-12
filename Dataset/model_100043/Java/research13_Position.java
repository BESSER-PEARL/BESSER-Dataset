





import java.util.List;
import java.util.ArrayList;

public class research13_Position extends Named {

    private String description;





    private research13_Researcher research13_researcher;




    private research13_Position research13_position;




    private research13_PublicationSystem research13_publicationsystem;


    public research13_Position(
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

    public research13_Researcher getResearch13_researcher() {
        return research13_researcher;
    }

    public void setResearch13_researcher(research13_Researcher research13_researcher) {
        this.research13_researcher = research13_researcher;
    }
    public research13_Position getResearch13_position() {
        return research13_position;
    }

    public void setResearch13_position(research13_Position research13_position) {
        this.research13_position = research13_position;
    }
    public research13_PublicationSystem getResearch13_publicationsystem() {
        return research13_publicationsystem;
    }

    public void setResearch13_publicationsystem(research13_PublicationSystem research13_publicationsystem) {
        this.research13_publicationsystem = research13_publicationsystem;
    }

}