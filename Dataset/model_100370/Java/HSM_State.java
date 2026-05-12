





import java.util.List;
import java.util.ArrayList;

public class HSM_State extends PrimitiveState {






    private OrState orstate;


    public HSM_State(
    ) {
        super(
        );
    }



    public OrState getOrstate() {
        return orstate;
    }

    public void setOrstate(OrState orstate) {
        this.orstate = orstate;
    }

}