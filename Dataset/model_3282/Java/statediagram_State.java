





import java.util.List;
import java.util.ArrayList;

public class statediagram_State  {

    private boolean isInitial;
    private String name;





    private statediagram_StateDiagram statediagram_statediagram;


    public statediagram_State(
        boolean isInitial,        String name    ) {
        this.isInitial = isInitial;
        this.name = name;
    }


    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statediagram_StateDiagram getStatediagram_statediagram() {
        return statediagram_statediagram;
    }

    public void setStatediagram_statediagram(statediagram_StateDiagram statediagram_statediagram) {
        this.statediagram_statediagram = statediagram_statediagram;
    }

}