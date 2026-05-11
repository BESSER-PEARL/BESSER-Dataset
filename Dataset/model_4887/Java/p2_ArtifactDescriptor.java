





import java.util.List;
import java.util.ArrayList;

public class p2_ArtifactDescriptor extends IArtifactDescriptor {






    private List<p2_Property> p2_propertys;




    private List<p2_IProcessingStepDescriptor> p2_iprocessingstepdescriptors;


    public p2_ArtifactDescriptor(
    ) {
        super(
        );
        this.p2_propertys = new ArrayList<>();
        this.p2_iprocessingstepdescriptors = new ArrayList<>();
    }

    public p2_ArtifactDescriptor(
        ArrayList<p2_Property> p2_propertys,        ArrayList<p2_IProcessingStepDescriptor> p2_iprocessingstepdescriptors    ) {
        this.p2_propertys = p2_propertys;
        this.p2_iprocessingstepdescriptors = p2_iprocessingstepdescriptors;
    }


    public List<p2_Property> getP2_propertys() {
        return p2_propertys;
    }

    public void addP2_property(P2_property p2_property) {
        this.p2_propertys.add(p2_property);
    }
    public List<p2_IProcessingStepDescriptor> getP2_iprocessingstepdescriptors() {
        return p2_iprocessingstepdescriptors;
    }

    public void addP2_iprocessingstepdescriptor(P2_iprocessingstepdescriptor p2_iprocessingstepdescriptor) {
        this.p2_iprocessingstepdescriptors.add(p2_iprocessingstepdescriptor);
    }

}