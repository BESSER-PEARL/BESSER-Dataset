





import java.util.List;
import java.util.ArrayList;

public class samplemodel_NodeTargetB extends CommonBaseClass {

    private String title;





    private List<samplemodel_Child> samplemodel_childs;




    private samplemodel_NodeSrcA samplemodel_nodesrca;




    private samplemodel_NodeSrcA samplemodel_nodesrca;




    private samplemodel_NodeSrcA samplemodel_nodesrca;


    public samplemodel_NodeTargetB(
        String title    ) {
        super(
        );
        this.title = title;
        this.samplemodel_childs = new ArrayList<>();
    }

    public samplemodel_NodeTargetB(
        String title        ArrayList<samplemodel_Child> samplemodel_childs    ) {
        this.title = title;
        this.samplemodel_childs = samplemodel_childs;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<samplemodel_Child> getSamplemodel_childs() {
        return samplemodel_childs;
    }

    public void addSamplemodel_child(Samplemodel_child samplemodel_child) {
        this.samplemodel_childs.add(samplemodel_child);
    }
    public samplemodel_NodeSrcA getSamplemodel_nodesrca() {
        return samplemodel_nodesrca;
    }

    public void setSamplemodel_nodesrca(samplemodel_NodeSrcA samplemodel_nodesrca) {
        this.samplemodel_nodesrca = samplemodel_nodesrca;
    }
    public samplemodel_NodeSrcA getSamplemodel_nodesrca() {
        return samplemodel_nodesrca;
    }

    public void setSamplemodel_nodesrca(samplemodel_NodeSrcA samplemodel_nodesrca) {
        this.samplemodel_nodesrca = samplemodel_nodesrca;
    }
    public samplemodel_NodeSrcA getSamplemodel_nodesrca() {
        return samplemodel_nodesrca;
    }

    public void setSamplemodel_nodesrca(samplemodel_NodeSrcA samplemodel_nodesrca) {
        this.samplemodel_nodesrca = samplemodel_nodesrca;
    }

}