





import java.util.List;
import java.util.ArrayList;

public class GraphMetaM_Graph  {

    private String name;
    private String rName;
    private int cycles;



    public GraphMetaM_Graph(
        String name,        String rName,        int cycles    ) {
        this.name = name;
        this.rName = rName;
        this.cycles = cycles;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRname() {
        return rName;
    }

    public void setRname(String rName) {
        this.rName = rName;
    }
    public int getCycles() {
        return cycles;
    }

    public void setCycles(int cycles) {
        this.cycles = cycles;
    }


}