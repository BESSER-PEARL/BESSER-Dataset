





import java.util.List;
import java.util.ArrayList;

public class iritpdl_WorkDefinition extends ProcessElement {

    private int minTime;
    private String name;
    private int maxTime;





    private iritpdl_ProcessElement iritpdl_processelement;




    private List<iritpdl_ProcessElement> iritpdl_processelements;


    public iritpdl_WorkDefinition(
        int minTime,        String name,        int maxTime    ) {
        super(
        );
        this.minTime = minTime;
        this.name = name;
        this.maxTime = maxTime;
        this.iritpdl_processelements = new ArrayList<>();
    }

    public iritpdl_WorkDefinition(
        int minTime,        String name,        int maxTime        ArrayList<iritpdl_ProcessElement> iritpdl_processelements    ) {
        this.minTime = minTime;
        this.name = name;
        this.maxTime = maxTime;
        this.iritpdl_processelements = iritpdl_processelements;
    }

    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(int maxTime) {
        this.maxTime = maxTime;
    }

    public iritpdl_ProcessElement getIritpdl_processelement() {
        return iritpdl_processelement;
    }

    public void setIritpdl_processelement(iritpdl_ProcessElement iritpdl_processelement) {
        this.iritpdl_processelement = iritpdl_processelement;
    }
    public List<iritpdl_ProcessElement> getIritpdl_processelements() {
        return iritpdl_processelements;
    }

    public void addIritpdl_processelement(Iritpdl_processelement iritpdl_processelement) {
        this.iritpdl_processelements.add(iritpdl_processelement);
    }

}