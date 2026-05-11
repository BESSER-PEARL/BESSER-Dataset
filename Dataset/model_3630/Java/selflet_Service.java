





import java.util.List;
import java.util.ArrayList;

public class selflet_Service  {

    private String maxResponseTime;
    private String revenue;
    private String name;
    private String active;





    private selflet_Output selflet_output;




    private selflet_Services selflet_services;




    private List<selflet_Behavior> selflet_behaviors;




    private selflet_Behavior selflet_behavior;




    private selflet_IntermediateState selflet_intermediatestate;


    public selflet_Service(
        String maxResponseTime,        String revenue,        String name,        String active    ) {
        this.maxResponseTime = maxResponseTime;
        this.revenue = revenue;
        this.name = name;
        this.active = active;
        this.selflet_behaviors = new ArrayList<>();
    }

    public selflet_Service(
        String maxResponseTime,        String revenue,        String name,        String active        ArrayList<selflet_Behavior> selflet_behaviors    ) {
        this.maxResponseTime = maxResponseTime;
        this.revenue = revenue;
        this.name = name;
        this.active = active;
        this.selflet_behaviors = selflet_behaviors;
    }

    public String getMaxresponsetime() {
        return maxResponseTime;
    }

    public void setMaxresponsetime(String maxResponseTime) {
        this.maxResponseTime = maxResponseTime;
    }
    public String getRevenue() {
        return revenue;
    }

    public void setRevenue(String revenue) {
        this.revenue = revenue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getActive() {
        return active;
    }

    public void setActive(String active) {
        this.active = active;
    }

    public selflet_Output getSelflet_output() {
        return selflet_output;
    }

    public void setSelflet_output(selflet_Output selflet_output) {
        this.selflet_output = selflet_output;
    }
    public selflet_Services getSelflet_services() {
        return selflet_services;
    }

    public void setSelflet_services(selflet_Services selflet_services) {
        this.selflet_services = selflet_services;
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
    public selflet_IntermediateState getSelflet_intermediatestate() {
        return selflet_intermediatestate;
    }

    public void setSelflet_intermediatestate(selflet_IntermediateState selflet_intermediatestate) {
        this.selflet_intermediatestate = selflet_intermediatestate;
    }

}