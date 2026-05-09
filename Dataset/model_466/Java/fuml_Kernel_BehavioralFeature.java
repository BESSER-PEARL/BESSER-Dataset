





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_BehavioralFeature extends Feature {

    private String concurrency;
    private boolean abstract;





    private List<BasicBehaviors_Behavior> basicbehaviors_behaviors;




    private List<Kernel_Parameter> kernel_parameters;


    public fuml_Kernel_BehavioralFeature(
        String concurrency,        boolean abstract    ) {
        super(
        );
        this.concurrency = concurrency;
        this.abstract = abstract;
        this.basicbehaviors_behaviors = new ArrayList<>();
        this.kernel_parameters = new ArrayList<>();
    }

    public fuml_Kernel_BehavioralFeature(
        String concurrency,        boolean abstract        ArrayList<BasicBehaviors_Behavior> basicbehaviors_behaviors,        ArrayList<Kernel_Parameter> kernel_parameters    ) {
        this.concurrency = concurrency;
        this.abstract = abstract;
        this.basicbehaviors_behaviors = basicbehaviors_behaviors;
        this.kernel_parameters = kernel_parameters;
    }

    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
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