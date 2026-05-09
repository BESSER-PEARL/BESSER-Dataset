





import java.util.List;
import java.util.ArrayList;

public class petrinet_Node extends Element {

    private float minDelay;
    private float maxDelay;
    private String name;



    public petrinet_Node(
        float minDelay,        float maxDelay,        String name    ) {
        super(
        );
        this.minDelay = minDelay;
        this.maxDelay = maxDelay;
        this.name = name;
    }


    public float getMindelay() {
        return minDelay;
    }

    public void setMindelay(float minDelay) {
        this.minDelay = minDelay;
    }
    public float getMaxdelay() {
        return maxDelay;
    }

    public void setMaxdelay(float maxDelay) {
        this.maxDelay = maxDelay;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}