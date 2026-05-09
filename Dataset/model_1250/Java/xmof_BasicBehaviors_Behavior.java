





import java.util.List;
import java.util.ArrayList;

public class xmof_BasicBehaviors_Behavior extends BehavioredEClass {

    private boolean reentrant;





    private List<Kernel_DirectedParameter> kernel_directedparameters;




    private BasicBehaviors_BehavioredClassifier basicbehaviors_behavioredclassifier;




    private Kernel_BehavioredEOperation kernel_behavioredeoperation;


    public xmof_BasicBehaviors_Behavior(
        boolean reentrant    ) {
        super(
        );
        this.reentrant = reentrant;
        this.kernel_directedparameters = new ArrayList<>();
    }

    public xmof_BasicBehaviors_Behavior(
        boolean reentrant        ArrayList<Kernel_DirectedParameter> kernel_directedparameters    ) {
        this.reentrant = reentrant;
        this.kernel_directedparameters = kernel_directedparameters;
    }

    public boolean getReentrant() {
        return reentrant;
    }

    public void setReentrant(boolean reentrant) {
        this.reentrant = reentrant;
    }

    public List<Kernel_DirectedParameter> getKernel_directedparameters() {
        return kernel_directedparameters;
    }

    public void addKernel_directedparameter(Kernel_directedparameter kernel_directedparameter) {
        this.kernel_directedparameters.add(kernel_directedparameter);
    }
    public BasicBehaviors_BehavioredClassifier getBasicbehaviors_behavioredclassifier() {
        return basicbehaviors_behavioredclassifier;
    }

    public void setBasicbehaviors_behavioredclassifier(BasicBehaviors_BehavioredClassifier basicbehaviors_behavioredclassifier) {
        this.basicbehaviors_behavioredclassifier = basicbehaviors_behavioredclassifier;
    }
    public Kernel_BehavioredEOperation getKernel_behavioredeoperation() {
        return kernel_behavioredeoperation;
    }

    public void setKernel_behavioredeoperation(Kernel_BehavioredEOperation kernel_behavioredeoperation) {
        this.kernel_behavioredeoperation = kernel_behavioredeoperation;
    }

}