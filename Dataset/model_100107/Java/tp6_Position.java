





import java.util.List;
import java.util.ArrayList;

public class tp6_Position  {

    private String description;
    private String name;





    private tp6_Position tp6_position;


    public tp6_Position(
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

    public tp6_Position getTp6_position() {
        return tp6_position;
    }

    public void setTp6_position(tp6_Position tp6_position) {
        this.tp6_position = tp6_position;
    }

}