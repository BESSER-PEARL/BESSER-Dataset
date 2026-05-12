





import java.util.List;
import java.util.ArrayList;

public class research31_Position extends Named {

    private String description;





    private research31_Position research31_position;




    private research31_Researcher research31_researcher;


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

    public research31_Position getResearch31_position() {
        return research31_position;
    }

    public void setResearch31_position(research31_Position research31_position) {
        this.research31_position = research31_position;
    }
    public research31_Researcher getResearch31_researcher() {
        return research31_researcher;
    }

    public void setResearch31_researcher(research31_Researcher research31_researcher) {
        this.research31_researcher = research31_researcher;
    }

}