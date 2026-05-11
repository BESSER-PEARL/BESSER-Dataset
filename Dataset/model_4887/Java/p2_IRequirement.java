





import java.util.List;
import java.util.ArrayList;

public class p2_IRequirement  {

    private String max;
    private String min;
    private boolean greedy;
    private String description;
    private String matches;
    private String filter;





    private p2_IInstallableUnitPatch p2_iinstallableunitpatch;




    private p2_IInstallableUnit p2_iinstallableunit;




    private p2_IInstallableUnit p2_iinstallableunit;




    private p2_IInstallableUnitPatch p2_iinstallableunitpatch;


    public p2_IRequirement(
        String max,        String min,        boolean greedy,        String description,        String matches,        String filter    ) {
        this.max = max;
        this.min = min;
        this.greedy = greedy;
        this.description = description;
        this.matches = matches;
        this.filter = filter;
    }


    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
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
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }

    public p2_IInstallableUnitPatch getP2_iinstallableunitpatch() {
        return p2_iinstallableunitpatch;
    }

    public void setP2_iinstallableunitpatch(p2_IInstallableUnitPatch p2_iinstallableunitpatch) {
        this.p2_iinstallableunitpatch = p2_iinstallableunitpatch;
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
    public p2_IInstallableUnitPatch getP2_iinstallableunitpatch() {
        return p2_iinstallableunitpatch;
    }

    public void setP2_iinstallableunitpatch(p2_IInstallableUnitPatch p2_iinstallableunitpatch) {
        this.p2_iinstallableunitpatch = p2_iinstallableunitpatch;
    }

}