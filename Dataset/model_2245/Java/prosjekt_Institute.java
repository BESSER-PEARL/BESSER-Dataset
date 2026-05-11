





import java.util.List;
import java.util.ArrayList;

public class prosjekt_Institute  {

    private String name;
    private String shortName;



    public prosjekt_Institute(
        String name,        String shortName    ) {
        this.name = name;
        this.shortName = shortName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }


}