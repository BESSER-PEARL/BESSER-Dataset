





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Resource  {

    private String name;
    private int marking;





    private simplepdl_Process simplepdl_process;


    public simplepdl_Resource(
        String name,        int marking    ) {
        this.name = name;
        this.marking = marking;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMarking() {
        return marking;
    }

    public void setMarking(int marking) {
        this.marking = marking;
    }

    public simplepdl_Process getSimplepdl_process() {
        return simplepdl_process;
    }

    public void setSimplepdl_process(simplepdl_Process simplepdl_process) {
        this.simplepdl_process = simplepdl_process;
    }

}