





import java.util.List;
import java.util.ArrayList;

public class research2_Position extends Named {

    private String description;





    private research2_PublicationSystem research2_publicationsystem;




    private research2_Researcher research2_researcher;




    private research2_Position research2_position;


    public research2_Position(
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

    public research2_PublicationSystem getResearch2_publicationsystem() {
        return research2_publicationsystem;
    }

    public void setResearch2_publicationsystem(research2_PublicationSystem research2_publicationsystem) {
        this.research2_publicationsystem = research2_publicationsystem;
    }
    public research2_Researcher getResearch2_researcher() {
        return research2_researcher;
    }

    public void setResearch2_researcher(research2_Researcher research2_researcher) {
        this.research2_researcher = research2_researcher;
    }
    public research2_Position getResearch2_position() {
        return research2_position;
    }

    public void setResearch2_position(research2_Position research2_position) {
        this.research2_position = research2_position;
    }

}