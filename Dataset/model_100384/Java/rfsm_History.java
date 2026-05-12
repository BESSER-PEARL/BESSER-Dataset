





import java.util.List;
import java.util.ArrayList;

public class rfsm_History  {

    private int depth;
    private boolean hot;





    private rfsm_Connector rfsm_connector;


    public rfsm_History(
        int depth,        boolean hot    ) {
        this.depth = depth;
        this.hot = hot;
    }


    public int getDepth() {
        return depth;
    }

    public void setDepth(int depth) {
        this.depth = depth;
    }
    public boolean getHot() {
        return hot;
    }

    public void setHot(boolean hot) {
        this.hot = hot;
    }

    public rfsm_Connector getRfsm_connector() {
        return rfsm_connector;
    }

    public void setRfsm_connector(rfsm_Connector rfsm_connector) {
        this.rfsm_connector = rfsm_connector;
    }

}