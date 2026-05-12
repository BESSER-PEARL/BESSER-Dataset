





import java.util.List;
import java.util.ArrayList;

public class build_BuilderConcernContext extends BuildConcernContext {

    private String outputAnnotationsRemovals;
    private boolean removePreCondition;
    private boolean matchParameters;
    private String sourceAnnotationsRemovals;
    private boolean varArgs;
    private boolean removePostCondition;
    private boolean removePostInputCondition;





    private List<build_ProvidesPredicate> build_providespredicates;




    private List<build_InputPredicate> build_inputpredicates;


    public build_BuilderConcernContext(
        String outputAnnotationsRemovals,        boolean removePreCondition,        boolean matchParameters,        String sourceAnnotationsRemovals,        boolean varArgs,        boolean removePostCondition,        boolean removePostInputCondition    ) {
        super(
        );
        this.outputAnnotationsRemovals = outputAnnotationsRemovals;
        this.removePreCondition = removePreCondition;
        this.matchParameters = matchParameters;
        this.sourceAnnotationsRemovals = sourceAnnotationsRemovals;
        this.varArgs = varArgs;
        this.removePostCondition = removePostCondition;
        this.removePostInputCondition = removePostInputCondition;
        this.build_providespredicates = new ArrayList<>();
        this.build_inputpredicates = new ArrayList<>();
    }

    public build_BuilderConcernContext(
        String outputAnnotationsRemovals,        boolean removePreCondition,        boolean matchParameters,        String sourceAnnotationsRemovals,        boolean varArgs,        boolean removePostCondition,        boolean removePostInputCondition        ArrayList<build_ProvidesPredicate> build_providespredicates,        ArrayList<build_InputPredicate> build_inputpredicates    ) {
        this.outputAnnotationsRemovals = outputAnnotationsRemovals;
        this.removePreCondition = removePreCondition;
        this.matchParameters = matchParameters;
        this.sourceAnnotationsRemovals = sourceAnnotationsRemovals;
        this.varArgs = varArgs;
        this.removePostCondition = removePostCondition;
        this.removePostInputCondition = removePostInputCondition;
        this.build_providespredicates = build_providespredicates;
        this.build_inputpredicates = build_inputpredicates;
    }

    public String getOutputannotationsremovals() {
        return outputAnnotationsRemovals;
    }

    public void setOutputannotationsremovals(String outputAnnotationsRemovals) {
        this.outputAnnotationsRemovals = outputAnnotationsRemovals;
    }
    public boolean getRemoveprecondition() {
        return removePreCondition;
    }

    public void setRemoveprecondition(boolean removePreCondition) {
        this.removePreCondition = removePreCondition;
    }
    public boolean getMatchparameters() {
        return matchParameters;
    }

    public void setMatchparameters(boolean matchParameters) {
        this.matchParameters = matchParameters;
    }
    public String getSourceannotationsremovals() {
        return sourceAnnotationsRemovals;
    }

    public void setSourceannotationsremovals(String sourceAnnotationsRemovals) {
        this.sourceAnnotationsRemovals = sourceAnnotationsRemovals;
    }
    public boolean getVarargs() {
        return varArgs;
    }

    public void setVarargs(boolean varArgs) {
        this.varArgs = varArgs;
    }
    public boolean getRemovepostcondition() {
        return removePostCondition;
    }

    public void setRemovepostcondition(boolean removePostCondition) {
        this.removePostCondition = removePostCondition;
    }
    public boolean getRemovepostinputcondition() {
        return removePostInputCondition;
    }

    public void setRemovepostinputcondition(boolean removePostInputCondition) {
        this.removePostInputCondition = removePostInputCondition;
    }

    public List<build_ProvidesPredicate> getBuild_providespredicates() {
        return build_providespredicates;
    }

    public void addBuild_providespredicate(Build_providespredicate build_providespredicate) {
        this.build_providespredicates.add(build_providespredicate);
    }
    public List<build_InputPredicate> getBuild_inputpredicates() {
        return build_inputpredicates;
    }

    public void addBuild_inputpredicate(Build_inputpredicate build_inputpredicate) {
        this.build_inputpredicates.add(build_inputpredicate);
    }

}