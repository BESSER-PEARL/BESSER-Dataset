





import java.util.List;
import java.util.ArrayList;

public class ptn103_AbstractTransition extends AbstractNode {

    private String guard;



    public ptn103_AbstractTransition(
        String guard    ) {
        super(
        );
        this.guard = guard;
    }


    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }


}