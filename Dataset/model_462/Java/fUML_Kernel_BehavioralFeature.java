





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_BehavioralFeature extends Feature {

    private boolean abstract;
    private String concurrency;





    private List<BasicBehaviors_Behavior> basicbehaviors_behaviors;




    private List<Kernel_Parameter> kernel_parameters;


    public fUML_Kernel_BehavioralFeature(
        boolean abstract,        String concurrency    ) {
        super(
        );
        this.abstract = abstract;
        this.concurrency = concurrency;
        this.basicbehaviors_behaviors = new ArrayList<>();
        this.kernel_parameters = new ArrayList<>();
    }

    public fUML_Kernel_BehavioralFeature(
        boolean abstract,        String concurrency        ArrayList<BasicBehaviors_Behavior> basicbehaviors_behaviors,        ArrayList<Kernel_Parameter> kernel_parameters    ) {
        this.abstract = abstract;
        this.concurrency = concurrency;
        this.basicbehaviors_behaviors = basicbehaviors_behaviors;
        this.kernel_parameters = kernel_parameters;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
    }

    public List<BasicBehaviors_Behavior> getBasicbehaviors_behaviors() {
        return basicbehaviors_behaviors;
    }

    public void addBasicbehaviors_behavior(Basicbehaviors_behavior basicbehaviors_behavior) {
        this.basicbehaviors_behaviors.add(basicbehaviors_behavior);
    }
    public List<Kernel_Parameter> getKernel_parameters() {
        return kernel_parameters;
    }

    public void addKernel_parameter(Kernel_parameter kernel_parameter) {
        this.kernel_parameters.add(kernel_parameter);
    }

}