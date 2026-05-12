





import java.util.List;
import java.util.ArrayList;

public class tp6_Researcher  {

    private String name;
    private String forName;



    public tp6_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
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