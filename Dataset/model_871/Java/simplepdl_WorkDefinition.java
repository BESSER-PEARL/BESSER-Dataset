





import java.util.List;
import java.util.ArrayList;

public class simplepdl_WorkDefinition extends ProcessElement {

    private int min_time;
    private int max_time;
    private String name;





    private simplepdl_WorkSequence simplepdl_worksequence;




    private List<simplepdl_WorkSequence> simplepdl_worksequences;




    private simplepdl_WorkSequence simplepdl_worksequence;




    private List<simplepdl_WorkSequence> simplepdl_worksequences;


    public simplepdl_WorkDefinition(
        int min_time,        int max_time,        String name    ) {
        super(
        );
        this.min_time = min_time;
        this.max_time = max_time;
        this.name = name;
        this.simplepdl_worksequences = new ArrayList<>();
        this.simplepdl_worksequences = new ArrayList<>();
    }

    public simplepdl_WorkDefinition(
        int min_time,        int max_time,        String name        ArrayList<simplepdl_WorkSequence> simplepdl_worksequences,        ArrayList<simplepdl_WorkSequence> simplepdl_worksequences    ) {
        this.min_time = min_time;
        this.max_time = max_time;
        this.name = name;
        this.simplepdl_worksequences = simplepdl_worksequences;
        this.simplepdl_worksequences = simplepdl_worksequences;
    }

    public int getMin_time() {
        return min_time;
    }

    public void setMin_time(int min_time) {
        this.min_time = min_time;
    }
    public int getMax_time() {
        return max_time;
    }

    public void setMax_time(int max_time) {
        this.max_time = max_time;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplepdl_WorkSequence getSimplepdl_worksequence() {
        return simplepdl_worksequence;
    }

    public void setSimplepdl_worksequence(simplepdl_WorkSequence simplepdl_worksequence) {
        this.simplepdl_worksequence = simplepdl_worksequence;
    }
    public List<simplepdl_WorkSequence> getSimplepdl_worksequences() {
        return simplepdl_worksequences;
    }

    public void addSimplepdl_worksequence(Simplepdl_worksequence simplepdl_worksequence) {
        this.simplepdl_worksequences.add(simplepdl_worksequence);
    }
    public simplepdl_WorkSequence getSimplepdl_worksequence() {
        return simplepdl_worksequence;
    }

    public void setSimplepdl_worksequence(simplepdl_WorkSequence simplepdl_worksequence) {
        this.simplepdl_worksequence = simplepdl_worksequence;
    }
    public List<simplepdl_WorkSequence> getSimplepdl_worksequences() {
        return simplepdl_worksequences;
    }

    public void addSimplepdl_worksequence(Simplepdl_worksequence simplepdl_worksequence) {
        this.simplepdl_worksequences.add(simplepdl_worksequence);
    }

}