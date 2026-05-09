





import java.util.List;
import java.util.ArrayList;

public class graphbt_Edge  {

    private String branch;
    private String composition;



    public graphbt_Edge(
        String branch,        String composition    ) {
        this.branch = branch;
        this.composition = composition;
    }


    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }
    public String getComposition() {
        return composition;
    }

    public void setComposition(String composition) {
        this.composition = composition;
    }


}