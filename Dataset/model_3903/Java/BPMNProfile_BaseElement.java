





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BaseElement  {

    private String id;





    private List<BPMNProfile_Documentation> bpmnprofile_documentations;




    private List<BPMNProfile_BPMNAssociation> bpmnprofile_bpmnassociations;




    private List<BPMNProfile_BPMNAssociation> bpmnprofile_bpmnassociations;




    private BPMNProfile_BPMNAssociation bpmnprofile_bpmnassociation;




    private List<BPMNProfile_ExtensionDefinition> bpmnprofile_extensiondefinitions;




    private BPMNProfile_Lane bpmnprofile_lane;




    private BPMNProfile_BPMNAssociation bpmnprofile_bpmnassociation;


    public BPMNProfile_BaseElement(
        String id    ) {
        this.id = id;
        this.bpmnprofile_documentations = new ArrayList<>();
        this.bpmnprofile_bpmnassociations = new ArrayList<>();
        this.bpmnprofile_bpmnassociations = new ArrayList<>();
        this.bpmnprofile_extensiondefinitions = new ArrayList<>();
    }

    public BPMNProfile_BaseElement(
        String id        ArrayList<BPMNProfile_Documentation> bpmnprofile_documentations,        ArrayList<BPMNProfile_BPMNAssociation> bpmnprofile_bpmnassociations,        ArrayList<BPMNProfile_BPMNAssociation> bpmnprofile_bpmnassociations,        ArrayList<BPMNProfile_ExtensionDefinition> bpmnprofile_extensiondefinitions    ) {
        this.id = id;
        this.bpmnprofile_documentations = bpmnprofile_documentations;
        this.bpmnprofile_bpmnassociations = bpmnprofile_bpmnassociations;
        this.bpmnprofile_bpmnassociations = bpmnprofile_bpmnassociations;
        this.bpmnprofile_extensiondefinitions = bpmnprofile_extensiondefinitions;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<BPMNProfile_Documentation> getBpmnprofile_documentations() {
        return bpmnprofile_documentations;
    }

    public void addBpmnprofile_documentation(Bpmnprofile_documentation bpmnprofile_documentation) {
        this.bpmnprofile_documentations.add(bpmnprofile_documentation);
    }
    public List<BPMNProfile_BPMNAssociation> getBpmnprofile_bpmnassociations() {
        return bpmnprofile_bpmnassociations;
    }

    public void addBpmnprofile_bpmnassociation(Bpmnprofile_bpmnassociation bpmnprofile_bpmnassociation) {
        this.bpmnprofile_bpmnassociations.add(bpmnprofile_bpmnassociation);
    }
    public List<BPMNProfile_BPMNAssociation> getBpmnprofile_bpmnassociations() {
        return bpmnprofile_bpmnassociations;
    }

    public void addBpmnprofile_bpmnassociation(Bpmnprofile_bpmnassociation bpmnprofile_bpmnassociation) {
        this.bpmnprofile_bpmnassociations.add(bpmnprofile_bpmnassociation);
    }
    public BPMNProfile_BPMNAssociation getBpmnprofile_bpmnassociation() {
        return bpmnprofile_bpmnassociation;
    }

    public void setBpmnprofile_bpmnassociation(BPMNProfile_BPMNAssociation bpmnprofile_bpmnassociation) {
        this.bpmnprofile_bpmnassociation = bpmnprofile_bpmnassociation;
    }
    public List<BPMNProfile_ExtensionDefinition> getBpmnprofile_extensiondefinitions() {
        return bpmnprofile_extensiondefinitions;
    }

    public void addBpmnprofile_extensiondefinition(Bpmnprofile_extensiondefinition bpmnprofile_extensiondefinition) {
        this.bpmnprofile_extensiondefinitions.add(bpmnprofile_extensiondefinition);
    }
    public BPMNProfile_Lane getBpmnprofile_lane() {
        return bpmnprofile_lane;
    }

    public void setBpmnprofile_lane(BPMNProfile_Lane bpmnprofile_lane) {
        this.bpmnprofile_lane = bpmnprofile_lane;
    }
    public BPMNProfile_BPMNAssociation getBpmnprofile_bpmnassociation() {
        return bpmnprofile_bpmnassociation;
    }

    public void setBpmnprofile_bpmnassociation(BPMNProfile_BPMNAssociation bpmnprofile_bpmnassociation) {
        this.bpmnprofile_bpmnassociation = bpmnprofile_bpmnassociation;
    }

}