





import java.util.List;
import java.util.ArrayList;

public class graphbt_SpecialEdge  {

    private int destination;
    private String type;



    public graphbt_SpecialEdge(
        int destination,        String type    ) {
        this.destination = destination;
        this.type = type;
    }


    public int getDestination() {
        return destination;
    }

    public void setDestination(int destination) {
        this.destination = destination;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}