





import java.util.List;
import java.util.ArrayList;

public class build_RequiredCapability extends Capability {

    private int max;
    private int min;
    private boolean greedy;
    private String versionRange;





    private build_BuildUnit build_buildunit;




    private build_FragmentHost build_fragmenthost;


    public build_RequiredCapability(
        int max,        int min,        boolean greedy,        String versionRange    ) {
        super(
        );
        this.max = max;
        this.min = min;
        this.greedy = greedy;
        this.versionRange = versionRange;
    }


    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public boolean getGreedy() {
        return greedy;
    }

    public void setGreedy(boolean greedy) {
        this.greedy = greedy;
    }
    public String getVersionrange() {
        return versionRange;
    }

    public void setVersionrange(String versionRange) {
        this.versionRange = versionRange;
    }

    public build_BuildUnit getBuild_buildunit() {
        return build_buildunit;
    }

    public void setBuild_buildunit(build_BuildUnit build_buildunit) {
        this.build_buildunit = build_buildunit;
    }
    public build_FragmentHost getBuild_fragmenthost() {
        return build_fragmenthost;
    }

    public void setBuild_fragmenthost(build_FragmentHost build_fragmenthost) {
        this.build_fragmenthost = build_fragmenthost;
    }

}