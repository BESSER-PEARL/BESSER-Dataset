





import java.util.List;
import java.util.ArrayList;

public class p2_IRequirement  {

    private String min;
    private String max;
    private boolean greedy;
    private String filter;
    private String description;
    private String matches;





    private p2_IInstallableUnit p2_iinstallableunit;




    private p2_IInstallableUnit p2_iinstallableunit;


    public p2_IRequirement(
        String min,        String max,        boolean greedy,        String filter,        String description,        String matches    ) {
        this.min = min;
        this.max = max;
        this.greedy = greedy;
        this.filter = filter;
        this.description = description;
        this.matches = matches;
    }


    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
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

    public p2_IInstallableUnit getP2_iinstallableunit() {
        return p2_iinstallableunit;
    }

    public void setP2_iinstallableunit(p2_IInstallableUnit p2_iinstallableunit) {
        this.p2_iinstallableunit = p2_iinstallableunit;
    }
    public p2_IInstallableUnit getP2_iinstallableunit() {
        return p2_iinstallableunit;
    }

    public void setP2_iinstallableunit(p2_IInstallableUnit p2_iinstallableunit) {
        this.p2_iinstallableunit = p2_iinstallableunit;
    }

}