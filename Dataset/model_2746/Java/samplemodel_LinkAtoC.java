





import java.util.List;
import java.util.ArrayList;

public class samplemodel_LinkAtoC  {






    private List<samplemodel_LinkAtoC> samplemodel_linkatocs;


    public samplemodel_LinkAtoC(
    ) {
        this.samplemodel_linkatocs = new ArrayList<>();
    }

    public samplemodel_LinkAtoC(
        ArrayList<samplemodel_LinkAtoC> samplemodel_linkatocs    ) {
        this.samplemodel_linkatocs = samplemodel_linkatocs;
    }


    public List<samplemodel_LinkAtoC> getSamplemodel_linkatocs() {
        return samplemodel_linkatocs;
    }

    public void addSamplemodel_linkatoc(Samplemodel_linkatoc samplemodel_linkatoc) {
        this.samplemodel_linkatocs.add(samplemodel_linkatoc);
    }

}