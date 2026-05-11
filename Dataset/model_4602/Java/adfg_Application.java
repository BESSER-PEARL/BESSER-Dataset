





import java.util.List;
import java.util.ArrayList;

public class adfg_Application  {

    private int nbGraphs;
    private int nbProcessors;
    private String name;
    private String sourceCode;
    private boolean dynamicChecking;
    private String schedulingAlgorithm;



    public adfg_Application(
        int nbGraphs,        int nbProcessors,        String name,        String sourceCode,        boolean dynamicChecking,        String schedulingAlgorithm    ) {
        this.nbGraphs = nbGraphs;
        this.nbProcessors = nbProcessors;
        this.name = name;
        this.sourceCode = sourceCode;
        this.dynamicChecking = dynamicChecking;
        this.schedulingAlgorithm = schedulingAlgorithm;
    }


    public int getNbgraphs() {
        return nbGraphs;
    }

    public void setNbgraphs(int nbGraphs) {
        this.nbGraphs = nbGraphs;
    }
    public int getNbprocessors() {
        return nbProcessors;
    }

    public void setNbprocessors(int nbProcessors) {
        this.nbProcessors = nbProcessors;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSourcecode() {
        return sourceCode;
    }

    public void setSourcecode(String sourceCode) {
        this.sourceCode = sourceCode;
    }
    public boolean getDynamicchecking() {
        return dynamicChecking;
    }

    public void setDynamicchecking(boolean dynamicChecking) {
        this.dynamicChecking = dynamicChecking;
    }
    public String getSchedulingalgorithm() {
        return schedulingAlgorithm;
    }

    public void setSchedulingalgorithm(String schedulingAlgorithm) {
        this.schedulingAlgorithm = schedulingAlgorithm;
    }


}