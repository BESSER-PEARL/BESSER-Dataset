





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedArtifact extends uml_TracedClassifier, uml_TracedDeployedArtifact {






    private List<uml_TracedOperation> uml_tracedoperations;




    private uml_umlTrace_Artifact uml_umltrace_artifact;




    private List<uml_TracedManifestation> uml_tracedmanifestations;




    private List<uml_TracedProperty> uml_tracedpropertys;




    private List<uml_TracedArtifact> uml_tracedartifacts;


    public umlTrace_uml_TracedArtifact(
    ) {
        super(
        );
        this.uml_tracedoperations = new ArrayList<>();
        this.uml_tracedmanifestations = new ArrayList<>();
        this.uml_tracedpropertys = new ArrayList<>();
        this.uml_tracedartifacts = new ArrayList<>();
    }

    public umlTrace_uml_TracedArtifact(
        ArrayList<uml_TracedOperation> uml_tracedoperations,        ArrayList<uml_TracedManifestation> uml_tracedmanifestations,        ArrayList<uml_TracedProperty> uml_tracedpropertys,        ArrayList<uml_TracedArtifact> uml_tracedartifacts    ) {
        this.uml_tracedoperations = uml_tracedoperations;
        this.uml_tracedmanifestations = uml_tracedmanifestations;
        this.uml_tracedpropertys = uml_tracedpropertys;
        this.uml_tracedartifacts = uml_tracedartifacts;
    }


    public List<uml_TracedOperation> getUml_tracedoperations() {
        return uml_tracedoperations;
    }

    public void addUml_tracedoperation(Uml_tracedoperation uml_tracedoperation) {
        this.uml_tracedoperations.add(uml_tracedoperation);
    }
    public uml_umlTrace_Artifact getUml_umltrace_artifact() {
        return uml_umltrace_artifact;
    }

    public void setUml_umltrace_artifact(uml_umlTrace_Artifact uml_umltrace_artifact) {
        this.uml_umltrace_artifact = uml_umltrace_artifact;
    }
    public List<uml_TracedManifestation> getUml_tracedmanifestations() {
        return uml_tracedmanifestations;
    }

    public void addUml_tracedmanifestation(Uml_tracedmanifestation uml_tracedmanifestation) {
        this.uml_tracedmanifestations.add(uml_tracedmanifestation);
    }
    public List<uml_TracedProperty> getUml_tracedpropertys() {
        return uml_tracedpropertys;
    }

    public void addUml_tracedproperty(Uml_tracedproperty uml_tracedproperty) {
        this.uml_tracedpropertys.add(uml_tracedproperty);
    }
    public List<uml_TracedArtifact> getUml_tracedartifacts() {
        return uml_tracedartifacts;
    }

    public void addUml_tracedartifact(Uml_tracedartifact uml_tracedartifact) {
        this.uml_tracedartifacts.add(uml_tracedartifact);
    }

}