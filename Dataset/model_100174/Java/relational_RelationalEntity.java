





import java.util.List;
import java.util.ArrayList;

public class relational_RelationalEntity  {

    private String nameInSource;
    private String name;



    public relational_RelationalEntity(
        String nameInSource,        String name    ) {
        this.nameInSource = nameInSource;
        this.name = name;
    }


    public String getNameinsource() {
        return nameInSource;
    }

    public void setNameinsource(String nameInSource) {
        this.nameInSource = nameInSource;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}