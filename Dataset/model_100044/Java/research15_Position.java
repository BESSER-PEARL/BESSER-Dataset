





import java.util.List;
import java.util.ArrayList;

public class research15_Position extends Named {

    private String description;





    private research15_PublicationSystem research15_publicationsystem;




    private research15_Position research15_position;


    public research15_Position(
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

    public research15_PublicationSystem getResearch15_publicationsystem() {
        return research15_publicationsystem;
    }

    public void setResearch15_publicationsystem(research15_PublicationSystem research15_publicationsystem) {
        this.research15_publicationsystem = research15_publicationsystem;
    }
    public research15_Position getResearch15_position() {
        return research15_position;
    }

    public void setResearch15_position(research15_Position research15_position) {
        this.research15_position = research15_position;
    }

}