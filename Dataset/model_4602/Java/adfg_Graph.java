





import java.util.List;
import java.util.ArrayList;

public class adfg_Graph  {

    private int id;
    private int bufferingRequirements;
    private String sourceCode;
    private int nbBuffers;
    private int nbActors;
    private float processorUtilization;
    private String name;





    private adfg_Application adfg_application;




    private adfg_Application adfg_application;


    public adfg_Graph(
        int id,        int bufferingRequirements,        String sourceCode,        int nbBuffers,        int nbActors,        float processorUtilization,        String name    ) {
        this.id = id;
        this.bufferingRequirements = bufferingRequirements;
        this.sourceCode = sourceCode;
        this.nbBuffers = nbBuffers;
        this.nbActors = nbActors;
        this.processorUtilization = processorUtilization;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getBufferingrequirements() {
        return bufferingRequirements;
    }

    public void setBufferingrequirements(int bufferingRequirements) {
        this.bufferingRequirements = bufferingRequirements;
    }
    public String getSourcecode() {
        return sourceCode;
    }

    public void setSourcecode(String sourceCode) {
        this.sourceCode = sourceCode;
    }
    public int getNbbuffers() {
        return nbBuffers;
    }

    public void setNbbuffers(int nbBuffers) {
        this.nbBuffers = nbBuffers;
    }
    public int getNbactors() {
        return nbActors;
    }

    public void setNbactors(int nbActors) {
        this.nbActors = nbActors;
    }
    public float getProcessorutilization() {
        return processorUtilization;
    }

    public void setProcessorutilization(float processorUtilization) {
        this.processorUtilization = processorUtilization;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adfg_Application getAdfg_application() {
        return adfg_application;
    }

    public void setAdfg_application(adfg_Application adfg_application) {
        this.adfg_application = adfg_application;
    }
    public adfg_Application getAdfg_application() {
        return adfg_application;
    }

    public void setAdfg_application(adfg_Application adfg_application) {
        this.adfg_application = adfg_application;
    }

}