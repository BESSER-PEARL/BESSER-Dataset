





import java.util.List;
import java.util.ArrayList;

public class actions_AtomicActionResult extends ActionResult {

    private float hasDensity;





    private actions_AtomicAction actions_atomicaction;


    public actions_AtomicActionResult(
        float hasDensity    ) {
        super(
        );
        this.hasDensity = hasDensity;
    }


    public float getHasdensity() {
        return hasDensity;
    }

    public void setHasdensity(float hasDensity) {
        this.hasDensity = hasDensity;
    }

    public actions_AtomicAction getActions_atomicaction() {
        return actions_atomicaction;
    }

    public void setActions_atomicaction(actions_AtomicAction actions_atomicaction) {
        this.actions_atomicaction = actions_atomicaction;
    }

}