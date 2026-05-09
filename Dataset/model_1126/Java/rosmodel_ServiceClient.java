





import java.util.List;
import java.util.ArrayList;

public class rosmodel_ServiceClient  {

    private String name;





    private rosmodel_Node rosmodel_node;




    private rosmodel_ServiceType rosmodel_servicetype;


    public rosmodel_ServiceClient(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rosmodel_Node getRosmodel_node() {
        return rosmodel_node;
    }

    public void setRosmodel_node(rosmodel_Node rosmodel_node) {
        this.rosmodel_node = rosmodel_node;
    }
    public rosmodel_ServiceType getRosmodel_servicetype() {
        return rosmodel_servicetype;
    }

    public void setRosmodel_servicetype(rosmodel_ServiceType rosmodel_servicetype) {
        this.rosmodel_servicetype = rosmodel_servicetype;
    }

}