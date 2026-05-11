





import java.util.List;
import java.util.ArrayList;

public class fault_tree_FailureInstance extends IDBase {

    private String name;





    private fault_tree_FailureType fault_tree_failuretype;




    private fault_tree_FailureInstance fault_tree_failureinstance;




    private fault_tree_FaultTree fault_tree_faulttree;




    private fault_tree_FaultTree fault_tree_faulttree;




    private fault_tree_ErrorInstance fault_tree_errorinstance;




    private fault_tree_FailureType fault_tree_failuretype;


    public fault_tree_FailureInstance(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fault_tree_FailureType getFault_tree_failuretype() {
        return fault_tree_failuretype;
    }

    public void setFault_tree_failuretype(fault_tree_FailureType fault_tree_failuretype) {
        this.fault_tree_failuretype = fault_tree_failuretype;
    }
    public fault_tree_FailureInstance getFault_tree_failureinstance() {
        return fault_tree_failureinstance;
    }

    public void setFault_tree_failureinstance(fault_tree_FailureInstance fault_tree_failureinstance) {
        this.fault_tree_failureinstance = fault_tree_failureinstance;
    }
    public fault_tree_FaultTree getFault_tree_faulttree() {
        return fault_tree_faulttree;
    }

    public void setFault_tree_faulttree(fault_tree_FaultTree fault_tree_faulttree) {
        this.fault_tree_faulttree = fault_tree_faulttree;
    }
    public fault_tree_FaultTree getFault_tree_faulttree() {
        return fault_tree_faulttree;
    }

    public void setFault_tree_faulttree(fault_tree_FaultTree fault_tree_faulttree) {
        this.fault_tree_faulttree = fault_tree_faulttree;
    }
    public fault_tree_ErrorInstance getFault_tree_errorinstance() {
        return fault_tree_errorinstance;
    }

    public void setFault_tree_errorinstance(fault_tree_ErrorInstance fault_tree_errorinstance) {
        this.fault_tree_errorinstance = fault_tree_errorinstance;
    }
    public fault_tree_FailureType getFault_tree_failuretype() {
        return fault_tree_failuretype;
    }

    public void setFault_tree_failuretype(fault_tree_FailureType fault_tree_failuretype) {
        this.fault_tree_failuretype = fault_tree_failuretype;
    }

}