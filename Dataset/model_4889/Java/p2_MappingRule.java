





import java.util.List;
import java.util.ArrayList;

public class p2_MappingRule  {

    private String output;
    private String filter;



    public p2_MappingRule(
        String output,        String filter    ) {
        this.output = output;
        this.filter = filter;
    }


    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }


}