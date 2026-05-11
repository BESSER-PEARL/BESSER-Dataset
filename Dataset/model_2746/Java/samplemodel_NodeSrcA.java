





import java.util.List;
import java.util.ArrayList;

public class samplemodel_NodeSrcA extends CommonBaseClass {

    private String label;





    private samplemodel_LinkAtoA samplemodel_linkatoa;




    private List<samplemodel_Child2> samplemodel_child2s;




    private samplemodel_LinkAtoC_Cardinality1 samplemodel_linkatoc_cardinality1;




    private samplemodel_NodeSrcA samplemodel_nodesrca;




    private List<samplemodel_LinkAtoC_Cardinality2> samplemodel_linkatoc_cardinality2s;




    private List<samplemodel_LinkAtoA> samplemodel_linkatoas;




    private List<samplemodel_Child> samplemodel_childs;




    private List<samplemodel_LinkAtoC> samplemodel_linkatocs;


    public samplemodel_NodeSrcA(
        String label    ) {
        super(
        );
        this.label = label;
        this.samplemodel_child2s = new ArrayList<>();
        this.samplemodel_linkatoc_cardinality2s = new ArrayList<>();
        this.samplemodel_linkatoas = new ArrayList<>();
        this.samplemodel_childs = new ArrayList<>();
        this.samplemodel_linkatocs = new ArrayList<>();
    }

    public samplemodel_NodeSrcA(
        String label        ArrayList<samplemodel_Child2> samplemodel_child2s,        ArrayList<samplemodel_LinkAtoC_Cardinality2> samplemodel_linkatoc_cardinality2s,        ArrayList<samplemodel_LinkAtoA> samplemodel_linkatoas,        ArrayList<samplemodel_Child> samplemodel_childs,        ArrayList<samplemodel_LinkAtoC> samplemodel_linkatocs    ) {
        this.label = label;
        this.samplemodel_child2s = samplemodel_child2s;
        this.samplemodel_linkatoc_cardinality2s = samplemodel_linkatoc_cardinality2s;
        this.samplemodel_linkatoas = samplemodel_linkatoas;
        this.samplemodel_childs = samplemodel_childs;
        this.samplemodel_linkatocs = samplemodel_linkatocs;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public samplemodel_LinkAtoA getSamplemodel_linkatoa() {
        return samplemodel_linkatoa;
    }

    public void setSamplemodel_linkatoa(samplemodel_LinkAtoA samplemodel_linkatoa) {
        this.samplemodel_linkatoa = samplemodel_linkatoa;
    }
    public List<samplemodel_Child2> getSamplemodel_child2s() {
        return samplemodel_child2s;
    }

    public void addSamplemodel_child2(Samplemodel_child2 samplemodel_child2) {
        this.samplemodel_child2s.add(samplemodel_child2);
    }
    public samplemodel_LinkAtoC_Cardinality1 getSamplemodel_linkatoc_cardinality1() {
        return samplemodel_linkatoc_cardinality1;
    }

    public void setSamplemodel_linkatoc_cardinality1(samplemodel_LinkAtoC_Cardinality1 samplemodel_linkatoc_cardinality1) {
        this.samplemodel_linkatoc_cardinality1 = samplemodel_linkatoc_cardinality1;
    }
    public samplemodel_NodeSrcA getSamplemodel_nodesrca() {
        return samplemodel_nodesrca;
    }

    public void setSamplemodel_nodesrca(samplemodel_NodeSrcA samplemodel_nodesrca) {
        this.samplemodel_nodesrca = samplemodel_nodesrca;
    }
    public List<samplemodel_LinkAtoC_Cardinality2> getSamplemodel_linkatoc_cardinality2s() {
        return samplemodel_linkatoc_cardinality2s;
    }

    public void addSamplemodel_linkatoc_cardinality2(Samplemodel_linkatoc_cardinality2 samplemodel_linkatoc_cardinality2) {
        this.samplemodel_linkatoc_cardinality2s.add(samplemodel_linkatoc_cardinality2);
    }
    public List<samplemodel_LinkAtoA> getSamplemodel_linkatoas() {
        return samplemodel_linkatoas;
    }

    public void addSamplemodel_linkatoa(Samplemodel_linkatoa samplemodel_linkatoa) {
        this.samplemodel_linkatoas.add(samplemodel_linkatoa);
    }
    public List<samplemodel_Child> getSamplemodel_childs() {
        return samplemodel_childs;
    }

    public void addSamplemodel_child(Samplemodel_child samplemodel_child) {
        this.samplemodel_childs.add(samplemodel_child);
    }
    public List<samplemodel_LinkAtoC> getSamplemodel_linkatocs() {
        return samplemodel_linkatocs;
    }

    public void addSamplemodel_linkatoc(Samplemodel_linkatoc samplemodel_linkatoc) {
        this.samplemodel_linkatocs.add(samplemodel_linkatoc);
    }

}