





import java.util.List;
import java.util.ArrayList;

public class research23_Position extends Named {

    private String description;





    private research23_PublicationSystem research23_publicationsystem;




    private research23_Position research23_position;


    public research23_Position(
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

    public research23_PublicationSystem getResearch23_publicationsystem() {
        return research23_publicationsystem;
    }

    public void setResearch23_publicationsystem(research23_PublicationSystem research23_publicationsystem) {
        this.research23_publicationsystem = research23_publicationsystem;
    }
    public research23_Position getResearch23_position() {
        return research23_position;
    }

    public void setResearch23_position(research23_Position research23_position) {
        this.research23_position = research23_position;
    }

}