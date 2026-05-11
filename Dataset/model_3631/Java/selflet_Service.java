





import java.util.List;
import java.util.ArrayList;

public class selflet_Service  {

    private String name;
    private String maxResponseTime;
    private String active;
    private String revenue;





    private List<selflet_Behavior> selflet_behaviors;




    private selflet_Behavior selflet_behavior;


    public selflet_Service(
        String name,        String maxResponseTime,        String active,        String revenue    ) {
        this.name = name;
        this.maxResponseTime = maxResponseTime;
        this.active = active;
        this.revenue = revenue;
        this.selflet_behaviors = new ArrayList<>();
    }

    public selflet_Service(
        String name,        String maxResponseTime,        String active,        String revenue        ArrayList<selflet_Behavior> selflet_behaviors    ) {
        this.name = name;
        this.maxResponseTime = maxResponseTime;
        this.active = active;
        this.revenue = revenue;
        this.selflet_behaviors = selflet_behaviors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMaxresponsetime() {
        return maxResponseTime;
    }

    public void setMaxresponsetime(String maxResponseTime) {
        this.maxResponseTime = maxResponseTime;
    }
    public String getActive() {
        return active;
    }

    public void setActive(String active) {
        this.active = active;
    }
    public String getRevenue() {
        return revenue;
    }

    public void setRevenue(String revenue) {
        this.revenue = revenue;
    }

    public List<selflet_Behavior> getSelflet_behaviors() {
        return selflet_behaviors;
    }

    public void addSelflet_behavior(Selflet_behavior selflet_behavior) {
        this.selflet_behaviors.add(selflet_behavior);
    }
    public selflet_Behavior getSelflet_behavior() {
        return selflet_behavior;
    }

    public void setSelflet_behavior(selflet_Behavior selflet_behavior) {
        this.selflet_behavior = selflet_behavior;
    }

}