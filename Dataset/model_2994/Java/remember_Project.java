





import java.util.List;
import java.util.ArrayList;

public class remember_Project  {

    private String description;
    private String projectId;
    private String projectNumber;





    private remember_Node remember_node;




    private remember_Customer remember_customer;




    private List<remember_Node> remember_nodes;




    private remember_Customer remember_customer;




    private remember_TimeSpent remember_timespent;


    public remember_Project(
        String description,        String projectId,        String projectNumber    ) {
        this.description = description;
        this.projectId = projectId;
        this.projectNumber = projectNumber;
        this.remember_nodes = new ArrayList<>();
    }

    public remember_Project(
        String description,        String projectId,        String projectNumber        ArrayList<remember_Node> remember_nodes    ) {
        this.description = description;
        this.projectId = projectId;
        this.projectNumber = projectNumber;
        this.remember_nodes = remember_nodes;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getProjectid() {
        return projectId;
    }

    public void setProjectid(String projectId) {
        this.projectId = projectId;
    }
    public String getProjectnumber() {
        return projectNumber;
    }

    public void setProjectnumber(String projectNumber) {
        this.projectNumber = projectNumber;
    }

    public remember_Node getRemember_node() {
        return remember_node;
    }

    public void setRemember_node(remember_Node remember_node) {
        this.remember_node = remember_node;
    }
    public remember_Customer getRemember_customer() {
        return remember_customer;
    }

    public void setRemember_customer(remember_Customer remember_customer) {
        this.remember_customer = remember_customer;
    }
    public List<remember_Node> getRemember_nodes() {
        return remember_nodes;
    }

    public void addRemember_node(Remember_node remember_node) {
        this.remember_nodes.add(remember_node);
    }
    public remember_Customer getRemember_customer() {
        return remember_customer;
    }

    public void setRemember_customer(remember_Customer remember_customer) {
        this.remember_customer = remember_customer;
    }
    public remember_TimeSpent getRemember_timespent() {
        return remember_timespent;
    }

    public void setRemember_timespent(remember_TimeSpent remember_timespent) {
        this.remember_timespent = remember_timespent;
    }

}