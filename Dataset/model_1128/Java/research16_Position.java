





import java.util.List;
import java.util.ArrayList;

public class research16_Position extends Named {

    private String description;





    private research16_PublicationSystem research16_publicationsystem;




    private research16_Position research16_position;


    public research16_Position(
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

    public research16_PublicationSystem getResearch16_publicationsystem() {
        return research16_publicationsystem;
    }

    public void setResearch16_publicationsystem(research16_PublicationSystem research16_publicationsystem) {
        this.research16_publicationsystem = research16_publicationsystem;
    }
    public research16_Position getResearch16_position() {
        return research16_position;
    }

    public void setResearch16_position(research16_Position research16_position) {
        this.research16_position = research16_position;
    }

}