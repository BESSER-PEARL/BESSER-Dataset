





import java.util.List;
import java.util.ArrayList;

public class petrinet_Arc  {

    private int weight;
    private String arcType;
    private String name;



    public petrinet_Arc(
        int weight,        String arcType,        String name    ) {
        this.weight = weight;
        this.arcType = arcType;
        this.name = name;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public String getArctype() {
        return arcType;
    }

    public void setArctype(String arcType) {
        this.arcType = arcType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}