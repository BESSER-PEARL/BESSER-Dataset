





import java.util.List;
import java.util.ArrayList;

public class properties_DatabaseAlias  {

    private String alias;
    private String id;



    public properties_DatabaseAlias(
        String alias,        String id    ) {
        this.alias = alias;
        this.id = id;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}