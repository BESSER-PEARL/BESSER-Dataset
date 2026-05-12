





import java.util.List;
import java.util.ArrayList;

public class research18_Position extends Named {

    private String description;





    private research18_Position research18_position;




    private research18_PublicationSystem research18_publicationsystem;


    public research18_Position(
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

    public research18_Position getResearch18_position() {
        return research18_position;
    }

    public void setResearch18_position(research18_Position research18_position) {
        this.research18_position = research18_position;
    }
    public research18_PublicationSystem getResearch18_publicationsystem() {
        return research18_publicationsystem;
    }

    public void setResearch18_publicationsystem(research18_PublicationSystem research18_publicationsystem) {
        this.research18_publicationsystem = research18_publicationsystem;
    }

}