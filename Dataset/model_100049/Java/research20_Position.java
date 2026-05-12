





import java.util.List;
import java.util.ArrayList;

public class research20_Position extends Named {

    private String description;





    private research20_PublicationSystem research20_publicationsystem;




    private research20_Position research20_position;


    public research20_Position(
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

    public research20_PublicationSystem getResearch20_publicationsystem() {
        return research20_publicationsystem;
    }

    public void setResearch20_publicationsystem(research20_PublicationSystem research20_publicationsystem) {
        this.research20_publicationsystem = research20_publicationsystem;
    }
    public research20_Position getResearch20_position() {
        return research20_position;
    }

    public void setResearch20_position(research20_Position research20_position) {
        this.research20_position = research20_position;
    }

}