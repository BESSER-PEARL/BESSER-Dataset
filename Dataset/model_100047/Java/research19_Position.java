





import java.util.List;
import java.util.ArrayList;

public class research19_Position extends Named {

    private String description;





    private research19_Position research19_position;


    public research19_Position(
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

    public research19_Position getResearch19_position() {
        return research19_position;
    }

    public void setResearch19_position(research19_Position research19_position) {
        this.research19_position = research19_position;
    }

}