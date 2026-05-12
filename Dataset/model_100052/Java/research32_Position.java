





import java.util.List;
import java.util.ArrayList;

public class research32_Position extends Named {

    private String description;





    private research32_Researcher research32_researcher;




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

    public research32_Researcher getResearch32_researcher() {
        return research32_researcher;
    }

    public void setResearch32_researcher(research32_Researcher research32_researcher) {
        this.research32_researcher = research32_researcher;
    }
    public research32_Position getResearch32_position() {
        return research32_position;
    }

    public void setResearch32_position(research32_Position research32_position) {
        this.research32_position = research32_position;
    }

}