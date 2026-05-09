





import java.util.List;
import java.util.ArrayList;

public class publication101_Position extends Named {

    private String description;





    private publication101_Position publication101_position;


    public publication101_Position(
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

    public publication101_Position getPublication101_position() {
        return publication101_position;
    }

    public void setPublication101_position(publication101_Position publication101_position) {
        this.publication101_position = publication101_position;
    }

}