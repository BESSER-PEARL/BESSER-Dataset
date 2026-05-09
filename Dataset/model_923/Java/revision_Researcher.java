





import java.util.List;
import java.util.ArrayList;

public class revision_Researcher  {

    private String position;
    private String name;
    private String forName;



    public revision_Researcher(
        String position,        String name,        String forName    ) {
        this.position = position;
        this.name = name;
        this.forName = forName;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getForname() {
        return forName;
    }

    public void setForname(String forName) {
        this.forName = forName;
    }


}