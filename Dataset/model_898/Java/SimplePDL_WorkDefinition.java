





import java.util.List;
import java.util.ArrayList;

public class SimplePDL_WorkDefinition extends ProcessElement {

    private int maxTime;
    private int minTime;
    private String name;





    private SimplePDL_WorkSequence simplepdl_worksequence;




    private List<SimplePDL_ProcessElement> simplepdl_processelements;




    private List<SimplePDL_WorkSequence> simplepdl_worksequences;




    private SimplePDL_ProcessElement simplepdl_processelement;




    private SimplePDL_Resource simplepdl_resource;




    private SimplePDL_WorkSequence simplepdl_worksequence;




    private List<SimplePDL_WorkSequence> simplepdl_worksequences;




    private List<SimplePDL_Resource> simplepdl_resources;


    public SimplePDL_WorkDefinition(
        int maxTime,        int minTime,        String name    ) {
        super(
        );
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.name = name;
        this.simplepdl_processelements = new ArrayList<>();
        this.simplepdl_worksequences = new ArrayList<>();
        this.simplepdl_worksequences = new ArrayList<>();
        this.simplepdl_resources = new ArrayList<>();
    }

    public SimplePDL_WorkDefinition(
        int maxTime,        int minTime,        String name        ArrayList<SimplePDL_ProcessElement> simplepdl_processelements,        ArrayList<SimplePDL_WorkSequence> simplepdl_worksequences,        ArrayList<SimplePDL_WorkSequence> simplepdl_worksequences,        ArrayList<SimplePDL_Resource> simplepdl_resources    ) {
        this.maxTime = maxTime;
        this.minTime = minTime;
        this.name = name;
        this.simplepdl_processelements = simplepdl_processelements;
        this.simplepdl_worksequences = simplepdl_worksequences;
        this.simplepdl_worksequences = simplepdl_worksequences;
        this.simplepdl_resources = simplepdl_resources;
    }

    public int getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(int maxTime) {
        this.maxTime = maxTime;
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

    public SimplePDL_WorkSequence getSimplepdl_worksequence() {
        return simplepdl_worksequence;
    }

    public void setSimplepdl_worksequence(SimplePDL_WorkSequence simplepdl_worksequence) {
        this.simplepdl_worksequence = simplepdl_worksequence;
    }
    public List<SimplePDL_ProcessElement> getSimplepdl_processelements() {
        return simplepdl_processelements;
    }

    public void addSimplepdl_processelement(Simplepdl_processelement simplepdl_processelement) {
        this.simplepdl_processelements.add(simplepdl_processelement);
    }
    public List<SimplePDL_WorkSequence> getSimplepdl_worksequences() {
        return simplepdl_worksequences;
    }

    public void addSimplepdl_worksequence(Simplepdl_worksequence simplepdl_worksequence) {
        this.simplepdl_worksequences.add(simplepdl_worksequence);
    }
    public SimplePDL_ProcessElement getSimplepdl_processelement() {
        return simplepdl_processelement;
    }

    public void setSimplepdl_processelement(SimplePDL_ProcessElement simplepdl_processelement) {
        this.simplepdl_processelement = simplepdl_processelement;
    }
    public SimplePDL_Resource getSimplepdl_resource() {
        return simplepdl_resource;
    }

    public void setSimplepdl_resource(SimplePDL_Resource simplepdl_resource) {
        this.simplepdl_resource = simplepdl_resource;
    }
    public SimplePDL_WorkSequence getSimplepdl_worksequence() {
        return simplepdl_worksequence;
    }

    public void setSimplepdl_worksequence(SimplePDL_WorkSequence simplepdl_worksequence) {
        this.simplepdl_worksequence = simplepdl_worksequence;
    }
    public List<SimplePDL_WorkSequence> getSimplepdl_worksequences() {
        return simplepdl_worksequences;
    }

    public void addSimplepdl_worksequence(Simplepdl_worksequence simplepdl_worksequence) {
        this.simplepdl_worksequences.add(simplepdl_worksequence);
    }
    public List<SimplePDL_Resource> getSimplepdl_resources() {
        return simplepdl_resources;
    }

    public void addSimplepdl_resource(Simplepdl_resource simplepdl_resource) {
        this.simplepdl_resources.add(simplepdl_resource);
    }

}