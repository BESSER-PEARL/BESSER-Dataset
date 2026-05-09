





import java.util.List;
import java.util.ArrayList;

public class sourceanalysator_GeneralSource  {

    private String aliases;
    private boolean dontCount;
    private String name;



    public sourceanalysator_GeneralSource(
        String aliases,        boolean dontCount,        String name    ) {
        this.aliases = aliases;
        this.dontCount = dontCount;
        this.name = name;
    }


    public String getAliases() {
        return aliases;
    }

    public void setAliases(String aliases) {
        this.aliases = aliases;
    }
    public boolean getDontcount() {
        return dontCount;
    }

    public void setDontcount(boolean dontCount) {
        this.dontCount = dontCount;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}