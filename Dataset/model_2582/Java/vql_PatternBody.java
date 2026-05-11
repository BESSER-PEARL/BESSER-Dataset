





import java.util.List;
import java.util.ArrayList;

public class vql_PatternBody  {

    private String name;





    private vql_Pattern vql_pattern;


    public vql_PatternBody(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vql_Pattern getVql_pattern() {
        return vql_pattern;
    }

    public void setVql_pattern(vql_Pattern vql_pattern) {
        this.vql_pattern = vql_pattern;
    }

}