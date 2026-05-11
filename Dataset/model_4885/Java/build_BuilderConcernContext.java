





import java.util.List;
import java.util.ArrayList;

public class build_BuilderConcernContext extends BuildConcernContext {

    private boolean varArgs;
    private boolean removePostCondition;
    private boolean matchParameters;
    private boolean removePreCondition;
    private boolean removePostInputCondition;
    private String outputAnnotationsRemovals;
    private String sourceAnnotationsRemovals;





    private List<build_ConditionalPathVector> build_conditionalpathvectors;




    private List<build_InputPredicate> build_inputpredicates;




    private build_BPropertySet build_bpropertyset;




    private build_BExpression build_bexpression;




    private List<build_ConditionalPathVector> build_conditionalpathvectors;




    private List<build_BuilderInput> build_builderinputs;




    private List<build_ProvidesPredicate> build_providespredicates;




    private build_BExpression build_bexpression;




    private build_UnitConcernContext build_unitconcerncontext;




    private List<build_BParameterPredicate> build_bparameterpredicates;




    private build_BExpression build_bexpression;




    private build_BExpression build_bexpression;




    private build_BPropertySet build_bpropertyset;




    private build_BExpression build_bexpression;


    public build_BuilderConcernContext(
        boolean varArgs,        boolean removePostCondition,        boolean matchParameters,        boolean removePreCondition,        boolean removePostInputCondition,        String outputAnnotationsRemovals,        String sourceAnnotationsRemovals    ) {
        super(
        );
        this.varArgs = varArgs;
        this.removePostCondition = removePostCondition;
        this.matchParameters = matchParameters;
        this.removePreCondition = removePreCondition;
        this.removePostInputCondition = removePostInputCondition;
        this.outputAnnotationsRemovals = outputAnnotationsRemovals;
        this.sourceAnnotationsRemovals = sourceAnnotationsRemovals;
        this.build_conditionalpathvectors = new ArrayList<>();
        this.build_inputpredicates = new ArrayList<>();
        this.build_conditionalpathvectors = new ArrayList<>();
        this.build_builderinputs = new ArrayList<>();
        this.build_providespredicates = new ArrayList<>();
        this.build_bparameterpredicates = new ArrayList<>();
    }

    public build_BuilderConcernContext(
        boolean varArgs,        boolean removePostCondition,        boolean matchParameters,        boolean removePreCondition,        boolean removePostInputCondition,        String outputAnnotationsRemovals,        String sourceAnnotationsRemovals        ArrayList<build_ConditionalPathVector> build_conditionalpathvectors,        ArrayList<build_InputPredicate> build_inputpredicates,        ArrayList<build_ConditionalPathVector> build_conditionalpathvectors,        ArrayList<build_BuilderInput> build_builderinputs,        ArrayList<build_ProvidesPredicate> build_providespredicates,        ArrayList<build_BParameterPredicate> build_bparameterpredicates    ) {
        this.varArgs = varArgs;
        this.removePostCondition = removePostCondition;
        this.matchParameters = matchParameters;
        this.removePreCondition = removePreCondition;
        this.removePostInputCondition = removePostInputCondition;
        this.outputAnnotationsRemovals = outputAnnotationsRemovals;
        this.sourceAnnotationsRemovals = sourceAnnotationsRemovals;
        this.build_conditionalpathvectors = build_conditionalpathvectors;
        this.build_inputpredicates = build_inputpredicates;
        this.build_conditionalpathvectors = build_conditionalpathvectors;
        this.build_builderinputs = build_builderinputs;
        this.build_providespredicates = build_providespredicates;
        this.build_bparameterpredicates = build_bparameterpredicates;
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
    public boolean getMatchparameters() {
        return matchParameters;
    }

    public void setMatchparameters(boolean matchParameters) {
        this.matchParameters = matchParameters;
    }
    public boolean getRemoveprecondition() {
        return removePreCondition;
    }

    public void setRemoveprecondition(boolean removePreCondition) {
        this.removePreCondition = removePreCondition;
    }
    public boolean getRemovepostinputcondition() {
        return removePostInputCondition;
    }

    public void setRemovepostinputcondition(boolean removePostInputCondition) {
        this.removePostInputCondition = removePostInputCondition;
    }
    public String getOutputannotationsremovals() {
        return outputAnnotationsRemovals;
    }

    public void setOutputannotationsremovals(String outputAnnotationsRemovals) {
        this.outputAnnotationsRemovals = outputAnnotationsRemovals;
    }
    public String getSourceannotationsremovals() {
        return sourceAnnotationsRemovals;
    }

    public void setSourceannotationsremovals(String sourceAnnotationsRemovals) {
        this.sourceAnnotationsRemovals = sourceAnnotationsRemovals;
    }

    public List<build_ConditionalPathVector> getBuild_conditionalpathvectors() {
        return build_conditionalpathvectors;
    }

    public void addBuild_conditionalpathvector(Build_conditionalpathvector build_conditionalpathvector) {
        this.build_conditionalpathvectors.add(build_conditionalpathvector);
    }
    public List<build_InputPredicate> getBuild_inputpredicates() {
        return build_inputpredicates;
    }

    public void addBuild_inputpredicate(Build_inputpredicate build_inputpredicate) {
        this.build_inputpredicates.add(build_inputpredicate);
    }
    public build_BPropertySet getBuild_bpropertyset() {
        return build_bpropertyset;
    }

    public void setBuild_bpropertyset(build_BPropertySet build_bpropertyset) {
        this.build_bpropertyset = build_bpropertyset;
    }
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }
    public List<build_ConditionalPathVector> getBuild_conditionalpathvectors() {
        return build_conditionalpathvectors;
    }

    public void addBuild_conditionalpathvector(Build_conditionalpathvector build_conditionalpathvector) {
        this.build_conditionalpathvectors.add(build_conditionalpathvector);
    }
    public List<build_BuilderInput> getBuild_builderinputs() {
        return build_builderinputs;
    }

    public void addBuild_builderinput(Build_builderinput build_builderinput) {
        this.build_builderinputs.add(build_builderinput);
    }
    public List<build_ProvidesPredicate> getBuild_providespredicates() {
        return build_providespredicates;
    }

    public void addBuild_providespredicate(Build_providespredicate build_providespredicate) {
        this.build_providespredicates.add(build_providespredicate);
    }
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }
    public build_UnitConcernContext getBuild_unitconcerncontext() {
        return build_unitconcerncontext;
    }

    public void setBuild_unitconcerncontext(build_UnitConcernContext build_unitconcerncontext) {
        this.build_unitconcerncontext = build_unitconcerncontext;
    }
    public List<build_BParameterPredicate> getBuild_bparameterpredicates() {
        return build_bparameterpredicates;
    }

    public void addBuild_bparameterpredicate(Build_bparameterpredicate build_bparameterpredicate) {
        this.build_bparameterpredicates.add(build_bparameterpredicate);
    }
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }
    public build_BPropertySet getBuild_bpropertyset() {
        return build_bpropertyset;
    }

    public void setBuild_bpropertyset(build_BPropertySet build_bpropertyset) {
        this.build_bpropertyset = build_bpropertyset;
    }
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }

}