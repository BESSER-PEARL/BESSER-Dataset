





import java.util.List;
import java.util.ArrayList;

public class research32_Position extends Named {

    private String description;





    private research32_PublicationSystem research32_publicationsystem;




    private research32_Position research32_position;


    public research32_Position(
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

    public research32_PublicationSystem getResearch32_publicationsystem() {
        return research32_publicationsystem;
    }

    public void setResearch32_publicationsystem(research32_PublicationSystem research32_publicationsystem) {
        this.research32_publicationsystem = research32_publicationsystem;
    }
    public research32_Position getResearch32_position() {
        return research32_position;
    }

    public void setResearch32_position(research32_Position research32_position) {
        this.research32_position = research32_position;
    }

}