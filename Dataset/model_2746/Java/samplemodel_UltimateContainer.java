





import java.util.List;
import java.util.ArrayList;

public class samplemodel_UltimateContainer  {

    private String diagramAttribute;





    private List<samplemodel_CommonBaseClass> samplemodel_commonbaseclasss;


    public samplemodel_UltimateContainer(
        String diagramAttribute    ) {
        this.diagramAttribute = diagramAttribute;
        this.samplemodel_commonbaseclasss = new ArrayList<>();
    }

    public samplemodel_UltimateContainer(
        String diagramAttribute        ArrayList<samplemodel_CommonBaseClass> samplemodel_commonbaseclasss    ) {
        this.diagramAttribute = diagramAttribute;
        this.samplemodel_commonbaseclasss = samplemodel_commonbaseclasss;
    }

    public String getDiagramattribute() {
        return diagramAttribute;
    }

    public void setDiagramattribute(String diagramAttribute) {
        this.diagramAttribute = diagramAttribute;
    }

    public List<samplemodel_CommonBaseClass> getSamplemodel_commonbaseclasss() {
        return samplemodel_commonbaseclasss;
    }

    public void addSamplemodel_commonbaseclass(Samplemodel_commonbaseclass samplemodel_commonbaseclass) {
        this.samplemodel_commonbaseclasss.add(samplemodel_commonbaseclass);
    }

}