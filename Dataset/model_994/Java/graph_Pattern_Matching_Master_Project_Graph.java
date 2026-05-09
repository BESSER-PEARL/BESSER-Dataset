





import java.util.List;
import java.util.ArrayList;

public class graph_Pattern_Matching_Master_Project_Graph  {

    private String name;
    private boolean direct;



    public graph_Pattern_Matching_Master_Project_Graph(
        String name,        boolean direct    ) {
        this.name = name;
        this.direct = direct;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getDirect() {
        return direct;
    }

    public void setDirect(boolean direct) {
        this.direct = direct;
    }


}