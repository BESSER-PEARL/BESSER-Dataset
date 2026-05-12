





import java.util.List;
import java.util.ArrayList;

public class publication105_Position extends Named {

    private String description;





    private publication105_Researcher publication105_researcher;




    private publication105_Position publication105_position;


    public publication105_Position(
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

    public publication105_Researcher getPublication105_researcher() {
        return publication105_researcher;
    }

    public void setPublication105_researcher(publication105_Researcher publication105_researcher) {
        this.publication105_researcher = publication105_researcher;
    }
    public publication105_Position getPublication105_position() {
        return publication105_position;
    }

    public void setPublication105_position(publication105_Position publication105_position) {
        this.publication105_position = publication105_position;
    }

}