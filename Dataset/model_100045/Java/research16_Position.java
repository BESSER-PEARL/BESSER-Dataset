





import java.util.List;
import java.util.ArrayList;

public class research16_Position extends Named {

    private String description;





    private research16_Position research16_position;




    private research16_Researcher research16_researcher;


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

    public research16_Position getResearch16_position() {
        return research16_position;
    }

    public void setResearch16_position(research16_Position research16_position) {
        this.research16_position = research16_position;
    }
    public research16_Researcher getResearch16_researcher() {
        return research16_researcher;
    }

    public void setResearch16_researcher(research16_Researcher research16_researcher) {
        this.research16_researcher = research16_researcher;
    }

}