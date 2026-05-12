





import java.util.List;
import java.util.ArrayList;

public class research101_Position extends Named {

    private String description;





    private research101_Position research101_position;




    private research101_PublicationSystem research101_publicationsystem;


    public research101_Position(
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

    public research101_Position getResearch101_position() {
        return research101_position;
    }

    public void setResearch101_position(research101_Position research101_position) {
        this.research101_position = research101_position;
    }
    public research101_PublicationSystem getResearch101_publicationsystem() {
        return research101_publicationsystem;
    }

    public void setResearch101_publicationsystem(research101_PublicationSystem research101_publicationsystem) {
        this.research101_publicationsystem = research101_publicationsystem;
    }

}