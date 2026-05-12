





import java.util.List;
import java.util.ArrayList;

public class tp5_Position  {

    private String description;
    private String name;





    private tp5_Position tp5_position;


    public tp5_Position(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tp5_Position getTp5_position() {
        return tp5_position;
    }

    public void setTp5_position(tp5_Position tp5_position) {
        this.tp5_position = tp5_position;
    }

}