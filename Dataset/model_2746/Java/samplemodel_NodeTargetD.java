





import java.util.List;
import java.util.ArrayList;

public class samplemodel_NodeTargetD extends NodeTargetB {






    private List<samplemodel_LinkAtoC> samplemodel_linkatocs;




    private samplemodel_LinkAtoC samplemodel_linkatoc;


    public samplemodel_NodeTargetD(
    ) {
        super(
        );
        this.samplemodel_linkatocs = new ArrayList<>();
    }

    public samplemodel_NodeTargetD(
        ArrayList<samplemodel_LinkAtoC> samplemodel_linkatocs    ) {
        this.samplemodel_linkatocs = samplemodel_linkatocs;
    }


    public List<samplemodel_LinkAtoC> getSamplemodel_linkatocs() {
        return samplemodel_linkatocs;
    }

    public void addSamplemodel_linkatoc(Samplemodel_linkatoc samplemodel_linkatoc) {
        this.samplemodel_linkatocs.add(samplemodel_linkatoc);
    }
    public samplemodel_LinkAtoC getSamplemodel_linkatoc() {
        return samplemodel_linkatoc;
    }

    public void setSamplemodel_linkatoc(samplemodel_LinkAtoC samplemodel_linkatoc) {
        this.samplemodel_linkatoc = samplemodel_linkatoc;
    }

}