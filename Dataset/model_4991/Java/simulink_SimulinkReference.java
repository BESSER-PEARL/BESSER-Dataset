





import java.util.List;
import java.util.ArrayList;

public class simulink_SimulinkReference  {

    private String name;
    private String qualifier;



    public simulink_SimulinkReference(
        String name,        String qualifier    ) {
        this.name = name;
        this.qualifier = qualifier;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }


}