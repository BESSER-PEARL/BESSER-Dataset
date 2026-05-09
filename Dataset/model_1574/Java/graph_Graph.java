





import java.util.List;
import java.util.ArrayList;

public class graph_Graph extends Named {

    private boolean direct;



    public graph_Graph(
        boolean direct    ) {
        super(
        );
        this.direct = direct;
    }


    public boolean getDirect() {
        return direct;
    }

    public void setDirect(boolean direct) {
        this.direct = direct;
    }


}