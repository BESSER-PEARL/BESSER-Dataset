





import java.util.List;
import java.util.ArrayList;

public class dtmc_NamedEntity  {

    private String name;
    private String description;



    public dtmc_NamedEntity(
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