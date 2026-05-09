





import java.util.List;
import java.util.ArrayList;

public class petrinet2_Place  {

    private String name;





    private petrinet2_Net petrinet2_net;


    public petrinet2_Place(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinet2_Net getPetrinet2_net() {
        return petrinet2_net;
    }

    public void setPetrinet2_net(petrinet2_Net petrinet2_net) {
        this.petrinet2_net = petrinet2_net;
    }

}