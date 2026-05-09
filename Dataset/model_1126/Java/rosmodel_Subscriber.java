





import java.util.List;
import java.util.ArrayList;

public class rosmodel_Subscriber  {

    private String name;
    private String msg;
    private int queue_size;





    private rosmodel_Topic rosmodel_topic;




    private rosmodel_Node rosmodel_node;


    public rosmodel_Subscriber(
        String name,        String msg,        int queue_size    ) {
        this.name = name;
        this.msg = msg;
        this.queue_size = queue_size;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }
    public int getQueue_size() {
        return queue_size;
    }

    public void setQueue_size(int queue_size) {
        this.queue_size = queue_size;
    }

    public rosmodel_Topic getRosmodel_topic() {
        return rosmodel_topic;
    }

    public void setRosmodel_topic(rosmodel_Topic rosmodel_topic) {
        this.rosmodel_topic = rosmodel_topic;
    }
    public rosmodel_Node getRosmodel_node() {
        return rosmodel_node;
    }

    public void setRosmodel_node(rosmodel_Node rosmodel_node) {
        this.rosmodel_node = rosmodel_node;
    }

}