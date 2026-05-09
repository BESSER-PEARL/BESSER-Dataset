





import java.util.List;
import java.util.ArrayList;

public class simplepdl_WorkDefinition extends ProcessElement {

    private String name;





    private simplepdl_WorkSequence simplepdl_worksequence;




    private List<simplepdl_Allocation> simplepdl_allocations;




    private List<simplepdl_WorkSequence> simplepdl_worksequences;




    private simplepdl_WorkSequence simplepdl_worksequence;




    private simplepdl_Allocation simplepdl_allocation;




    private List<simplepdl_WorkSequence> simplepdl_worksequences;


    public simplepdl_WorkDefinition(
        String name    ) {
        super(
        );
        this.name = name;
        this.simplepdl_allocations = new ArrayList<>();
        this.simplepdl_worksequences = new ArrayList<>();
        this.simplepdl_worksequences = new ArrayList<>();
    }

    public simplepdl_WorkDefinition(
        String name        ArrayList<simplepdl_Allocation> simplepdl_allocations,        ArrayList<simplepdl_WorkSequence> simplepdl_worksequences,        ArrayList<simplepdl_WorkSequence> simplepdl_worksequences    ) {
        this.name = name;
        this.simplepdl_allocations = simplepdl_allocations;
        this.simplepdl_worksequences = simplepdl_worksequences;
        this.simplepdl_worksequences = simplepdl_worksequences;
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
    public List<simplepdl_Allocation> getSimplepdl_allocations() {
        return simplepdl_allocations;
    }

    public void addSimplepdl_allocation(Simplepdl_allocation simplepdl_allocation) {
        this.simplepdl_allocations.add(simplepdl_allocation);
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
    public simplepdl_Allocation getSimplepdl_allocation() {
        return simplepdl_allocation;
    }

    public void setSimplepdl_allocation(simplepdl_Allocation simplepdl_allocation) {
        this.simplepdl_allocation = simplepdl_allocation;
    }
    public List<simplepdl_WorkSequence> getSimplepdl_worksequences() {
        return simplepdl_worksequences;
    }

    public void addSimplepdl_worksequence(Simplepdl_worksequence simplepdl_worksequence) {
        this.simplepdl_worksequences.add(simplepdl_worksequence);
    }

}