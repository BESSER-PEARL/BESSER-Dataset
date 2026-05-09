





import java.util.List;
import java.util.ArrayList;

public class publication103_Position extends Named {

    private String description;





    private publication103_Position publication103_position;


    public publication103_Position(
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

    public publication103_Position getPublication103_position() {
        return publication103_position;
    }

    public void setPublication103_position(publication103_Position publication103_position) {
        this.publication103_position = publication103_position;
    }

}