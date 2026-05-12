





import java.util.List;
import java.util.ArrayList;

public class publication102_Researcher  {

    private String forName;
    private String name;





    private publication102_Position publication102_position;


    public publication102_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
    }


    public String getForname() {
        return forName;
    }

    public void setForname(String forName) {
        this.forName = forName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public publication102_Position getPublication102_position() {
        return publication102_position;
    }

    public void setPublication102_position(publication102_Position publication102_position) {
        this.publication102_position = publication102_position;
    }

}