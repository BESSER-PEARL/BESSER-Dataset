





import java.util.List;
import java.util.ArrayList;

public class dot_Port  {

    private String name;
    private String compass_pt;





    private dot_Node dot_node;


    public dot_Port(
        String name,        String compass_pt    ) {
        this.name = name;
        this.compass_pt = compass_pt;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCompass_pt() {
        return compass_pt;
    }

    public void setCompass_pt(String compass_pt) {
        this.compass_pt = compass_pt;
    }

    public dot_Node getDot_node() {
        return dot_node;
    }

    public void setDot_node(dot_Node dot_node) {
        this.dot_node = dot_node;
    }

}