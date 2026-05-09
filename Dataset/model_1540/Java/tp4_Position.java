





import java.util.List;
import java.util.ArrayList;

public class tp4_Position extends Named {

    private String description;





    private tp4_Position tp4_position;


    public tp4_Position(
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

    public tp4_Position getTp4_position() {
        return tp4_position;
    }

    public void setTp4_position(tp4_Position tp4_position) {
        this.tp4_position = tp4_position;
    }

}