





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_MergeEvent extends Event {

    private int numberOfConflicts;
    private int totalTime;





    private List<operations_AbstractOperation> operations_abstractoperations;




    private versioning_PrimaryVersionSpec versioning_primaryversionspec;




    private versioning_PrimaryVersionSpec versioning_primaryversionspec;


    public esmodel_events_MergeEvent(
        int numberOfConflicts,        int totalTime    ) {
        super(
        );
        this.numberOfConflicts = numberOfConflicts;
        this.totalTime = totalTime;
        this.operations_abstractoperations = new ArrayList<>();
    }

    public esmodel_events_MergeEvent(
        int numberOfConflicts,        int totalTime        ArrayList<operations_AbstractOperation> operations_abstractoperations    ) {
        this.numberOfConflicts = numberOfConflicts;
        this.totalTime = totalTime;
        this.operations_abstractoperations = operations_abstractoperations;
    }

    public int getNumberofconflicts() {
        return numberOfConflicts;
    }

    public void setNumberofconflicts(int numberOfConflicts) {
        this.numberOfConflicts = numberOfConflicts;
    }
    public int getTotaltime() {
        return totalTime;
    }

    public void setTotaltime(int totalTime) {
        this.totalTime = totalTime;
    }

    public List<operations_AbstractOperation> getOperations_abstractoperations() {
        return operations_abstractoperations;
    }

    public void addOperations_abstractoperation(Operations_abstractoperation operations_abstractoperation) {
        this.operations_abstractoperations.add(operations_abstractoperation);
    }
    public versioning_PrimaryVersionSpec getVersioning_primaryversionspec() {
        return versioning_primaryversionspec;
    }

    public void setVersioning_primaryversionspec(versioning_PrimaryVersionSpec versioning_primaryversionspec) {
        this.versioning_primaryversionspec = versioning_primaryversionspec;
    }
    public versioning_PrimaryVersionSpec getVersioning_primaryversionspec() {
        return versioning_primaryversionspec;
    }

    public void setVersioning_primaryversionspec(versioning_PrimaryVersionSpec versioning_primaryversionspec) {
        this.versioning_primaryversionspec = versioning_primaryversionspec;
    }

}