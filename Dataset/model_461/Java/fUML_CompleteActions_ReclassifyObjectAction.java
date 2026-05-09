





import java.util.List;
import java.util.ArrayList;

public class fUML_CompleteActions_ReclassifyObjectAction extends Action {

    private boolean replaceAll;





    private List<Kernel_Classifier> kernel_classifiers;




    private BasicActions_InputPin basicactions_inputpin;




    private List<Kernel_Classifier> kernel_classifiers;


    public fUML_CompleteActions_ReclassifyObjectAction(
        boolean replaceAll    ) {
        super(
        );
        this.replaceAll = replaceAll;
        this.kernel_classifiers = new ArrayList<>();
        this.kernel_classifiers = new ArrayList<>();
    }

    public fUML_CompleteActions_ReclassifyObjectAction(
        boolean replaceAll        ArrayList<Kernel_Classifier> kernel_classifiers,        ArrayList<Kernel_Classifier> kernel_classifiers    ) {
        this.replaceAll = replaceAll;
        this.kernel_classifiers = kernel_classifiers;
        this.kernel_classifiers = kernel_classifiers;
    }

    public boolean getReplaceall() {
        return replaceAll;
    }

    public void setReplaceall(boolean replaceAll) {
        this.replaceAll = replaceAll;
    }

    public List<Kernel_Classifier> getKernel_classifiers() {
        return kernel_classifiers;
    }

    public void addKernel_classifier(Kernel_classifier kernel_classifier) {
        this.kernel_classifiers.add(kernel_classifier);
    }
    public BasicActions_InputPin getBasicactions_inputpin() {
        return basicactions_inputpin;
    }

    public void setBasicactions_inputpin(BasicActions_InputPin basicactions_inputpin) {
        this.basicactions_inputpin = basicactions_inputpin;
    }
    public List<Kernel_Classifier> getKernel_classifiers() {
        return kernel_classifiers;
    }

    public void addKernel_classifier(Kernel_classifier kernel_classifier) {
        this.kernel_classifiers.add(kernel_classifier);
    }

}