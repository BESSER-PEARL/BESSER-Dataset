





import java.util.List;
import java.util.ArrayList;

public class xs_RuleDeclaration extends Declaration {

    private int priority;
    private boolean runImmediately;
    private boolean highFrequency;
    private boolean active;
    private int minInterval;
    private String name;
    private int maxInterval;
    private String group;





    private xs_Block xs_block;


    public xs_RuleDeclaration(
        int priority,        boolean runImmediately,        boolean highFrequency,        boolean active,        int minInterval,        String name,        int maxInterval,        String group    ) {
        super(
        );
        this.priority = priority;
        this.runImmediately = runImmediately;
        this.highFrequency = highFrequency;
        this.active = active;
        this.minInterval = minInterval;
        this.name = name;
        this.maxInterval = maxInterval;
        this.group = group;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public boolean getRunimmediately() {
        return runImmediately;
    }

    public void setRunimmediately(boolean runImmediately) {
        this.runImmediately = runImmediately;
    }
    public boolean getHighfrequency() {
        return highFrequency;
    }

    public void setHighfrequency(boolean highFrequency) {
        this.highFrequency = highFrequency;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public int getMininterval() {
        return minInterval;
    }

    public void setMininterval(int minInterval) {
        this.minInterval = minInterval;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMaxinterval() {
        return maxInterval;
    }

    public void setMaxinterval(int maxInterval) {
        this.maxInterval = maxInterval;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public xs_Block getXs_block() {
        return xs_block;
    }

    public void setXs_block(xs_Block xs_block) {
        this.xs_block = xs_block;
    }

}