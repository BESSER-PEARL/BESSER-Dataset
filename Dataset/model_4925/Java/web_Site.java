





import java.util.List;
import java.util.ArrayList;

public class web_Site  {

    private String name;
    private String description;



    public web_Site(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}