





import java.util.List;
import java.util.ArrayList;

public class rosmodel_ActionServer  {

    private String name;





    private rosmodel_Node rosmodel_node;




    private rosmodel_ActionMessage rosmodel_actionmessage;


    public rosmodel_ActionServer(
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
    public rosmodel_ActionMessage getRosmodel_actionmessage() {
        return rosmodel_actionmessage;
    }

    public void setRosmodel_actionmessage(rosmodel_ActionMessage rosmodel_actionmessage) {
        this.rosmodel_actionmessage = rosmodel_actionmessage;
    }

}