





import java.util.List;
import java.util.ArrayList;

public class p2_MappingRule  {

    private String filter;
    private String output;



    public p2_MappingRule(
        String filter,        String output    ) {
        this.filter = filter;
        this.output = output;
    }


    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }


}