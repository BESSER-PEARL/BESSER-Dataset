





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Process  {

    private String name;





    private List<simplepdl_ProcessElement> simplepdl_processelements;


    public simplepdl_Process(
        String name    ) {
        this.name = name;
        this.simplepdl_processelements = new ArrayList<>();
    }

    public simplepdl_Process(
        String name        ArrayList<simplepdl_ProcessElement> simplepdl_processelements    ) {
        this.name = name;
        this.simplepdl_processelements = simplepdl_processelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<simplepdl_ProcessElement> getSimplepdl_processelements() {
        return simplepdl_processelements;
    }

    public void addSimplepdl_processelement(Simplepdl_processelement simplepdl_processelement) {
        this.simplepdl_processelements.add(simplepdl_processelement);
    }

}