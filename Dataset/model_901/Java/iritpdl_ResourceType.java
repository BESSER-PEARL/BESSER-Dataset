





import java.util.List;
import java.util.ArrayList;

public class iritpdl_ResourceType  {

    private int occurrences;
    private String name;





    private iritpdl_Process iritpdl_process;


    public iritpdl_ResourceType(
        int occurrences,        String name    ) {
        this.occurrences = occurrences;
        this.name = name;
    }


    public int getOccurrences() {
        return occurrences;
    }

    public void setOccurrences(int occurrences) {
        this.occurrences = occurrences;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iritpdl_Process getIritpdl_process() {
        return iritpdl_process;
    }

    public void setIritpdl_process(iritpdl_Process iritpdl_process) {
        this.iritpdl_process = iritpdl_process;
    }

}