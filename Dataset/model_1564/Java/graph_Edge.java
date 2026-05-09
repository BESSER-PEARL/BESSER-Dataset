





import java.util.List;
import java.util.ArrayList;

public class graph_Edge  {

    private boolean critical;



    public graph_Edge(
        boolean critical    ) {
        this.critical = critical;
    }


    public boolean getCritical() {
        return critical;
    }

    public void setCritical(boolean critical) {
        this.critical = critical;
    }


}