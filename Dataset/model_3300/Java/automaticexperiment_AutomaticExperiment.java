





import java.util.List;
import java.util.ArrayList;

public class automaticexperiment_AutomaticExperiment extends Identifiable {

    private String referanceDataDir;
    private float tolerance;
    private boolean reInit;
    private String errorFunction;
    private String errorAnalysisAlgorithm;
    private String maximumNumberOfIterations;





    private automaticexperiment_Scenario automaticexperiment_scenario;




    private List<automaticexperiment_ModifiableParameter> automaticexperiment_modifiableparameters;


    public automaticexperiment_AutomaticExperiment(
        String referanceDataDir,        float tolerance,        boolean reInit,        String errorFunction,        String errorAnalysisAlgorithm,        String maximumNumberOfIterations    ) {
        super(
        );
        this.referanceDataDir = referanceDataDir;
        this.tolerance = tolerance;
        this.reInit = reInit;
        this.errorFunction = errorFunction;
        this.errorAnalysisAlgorithm = errorAnalysisAlgorithm;
        this.maximumNumberOfIterations = maximumNumberOfIterations;
        this.automaticexperiment_modifiableparameters = new ArrayList<>();
    }

    public automaticexperiment_AutomaticExperiment(
        String referanceDataDir,        float tolerance,        boolean reInit,        String errorFunction,        String errorAnalysisAlgorithm,        String maximumNumberOfIterations        ArrayList<automaticexperiment_ModifiableParameter> automaticexperiment_modifiableparameters    ) {
        this.referanceDataDir = referanceDataDir;
        this.tolerance = tolerance;
        this.reInit = reInit;
        this.errorFunction = errorFunction;
        this.errorAnalysisAlgorithm = errorAnalysisAlgorithm;
        this.maximumNumberOfIterations = maximumNumberOfIterations;
        this.automaticexperiment_modifiableparameters = automaticexperiment_modifiableparameters;
    }

    public String getReferancedatadir() {
        return referanceDataDir;
    }

    public void setReferancedatadir(String referanceDataDir) {
        this.referanceDataDir = referanceDataDir;
    }
    public float getTolerance() {
        return tolerance;
    }

    public void setTolerance(float tolerance) {
        this.tolerance = tolerance;
    }
    public boolean getReinit() {
        return reInit;
    }

    public void setReinit(boolean reInit) {
        this.reInit = reInit;
    }
    public String getErrorfunction() {
        return errorFunction;
    }

    public void setErrorfunction(String errorFunction) {
        this.errorFunction = errorFunction;
    }
    public String getErroranalysisalgorithm() {
        return errorAnalysisAlgorithm;
    }

    public void setErroranalysisalgorithm(String errorAnalysisAlgorithm) {
        this.errorAnalysisAlgorithm = errorAnalysisAlgorithm;
    }
    public String getMaximumnumberofiterations() {
        return maximumNumberOfIterations;
    }

    public void setMaximumnumberofiterations(String maximumNumberOfIterations) {
        this.maximumNumberOfIterations = maximumNumberOfIterations;
    }

    public automaticexperiment_Scenario getAutomaticexperiment_scenario() {
        return automaticexperiment_scenario;
    }

    public void setAutomaticexperiment_scenario(automaticexperiment_Scenario automaticexperiment_scenario) {
        this.automaticexperiment_scenario = automaticexperiment_scenario;
    }
    public List<automaticexperiment_ModifiableParameter> getAutomaticexperiment_modifiableparameters() {
        return automaticexperiment_modifiableparameters;
    }

    public void addAutomaticexperiment_modifiableparameter(Automaticexperiment_modifiableparameter automaticexperiment_modifiableparameter) {
        this.automaticexperiment_modifiableparameters.add(automaticexperiment_modifiableparameter);
    }

}