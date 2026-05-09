





import java.util.List;
import java.util.ArrayList;

public class research31_Position extends Named {

    private String description;





    private research31_PublicationSystem research31_publicationsystem;




    private research31_Position research31_position;


    public research31_Position(
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

    public research31_PublicationSystem getResearch31_publicationsystem() {
        return research31_publicationsystem;
    }

    public void setResearch31_publicationsystem(research31_PublicationSystem research31_publicationsystem) {
        this.research31_publicationsystem = research31_publicationsystem;
    }
    public research31_Position getResearch31_position() {
        return research31_position;
    }

    public void setResearch31_position(research31_Position research31_position) {
        this.research31_position = research31_position;
    }

}