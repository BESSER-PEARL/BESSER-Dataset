





import java.util.List;
import java.util.ArrayList;

public class p2_IRequirement  {

    private String max;
    private String description;
    private String matches;
    private String min;
    private boolean greedy;
    private String filter;



    public p2_IRequirement(
        String max,        String description,        String matches,        String min,        boolean greedy,        String filter    ) {
        this.max = max;
        this.description = description;
        this.matches = matches;
        this.min = min;
        this.greedy = greedy;
        this.filter = filter;
    }


    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getMatches() {
        return matches;
    }

    public void setMatches(String matches) {
        this.matches = matches;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public boolean getGreedy() {
        return greedy;
    }

    public void setGreedy(boolean greedy) {
        this.greedy = greedy;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }


}