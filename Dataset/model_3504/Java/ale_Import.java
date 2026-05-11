





import java.util.List;
import java.util.ArrayList;

public class ale_Import  {

    private String name;
    private String alias;



    public ale_Import(
        String name,        String alias    ) {
        this.name = name;
        this.alias = alias;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }


}