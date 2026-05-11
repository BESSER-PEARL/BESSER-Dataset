





import java.util.List;
import java.util.ArrayList;

public class di_DocumentRoot  {

    private String mixed;





    private List<di_BPMNLabelStyle> di_bpmnlabelstyles;




    private List<di_BPMNPlane> di_bpmnplanes;




    private List<di_BPMNShape> di_bpmnshapes;




    private List<di_BPMNLabel> di_bpmnlabels;


    public di_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.di_bpmnlabelstyles = new ArrayList<>();
        this.di_bpmnplanes = new ArrayList<>();
        this.di_bpmnshapes = new ArrayList<>();
        this.di_bpmnlabels = new ArrayList<>();
    }

    public di_DocumentRoot(
        String mixed        ArrayList<di_BPMNLabelStyle> di_bpmnlabelstyles,        ArrayList<di_BPMNPlane> di_bpmnplanes,        ArrayList<di_BPMNShape> di_bpmnshapes,        ArrayList<di_BPMNLabel> di_bpmnlabels    ) {
        this.mixed = mixed;
        this.di_bpmnlabelstyles = di_bpmnlabelstyles;
        this.di_bpmnplanes = di_bpmnplanes;
        this.di_bpmnshapes = di_bpmnshapes;
        this.di_bpmnlabels = di_bpmnlabels;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<di_BPMNLabelStyle> getDi_bpmnlabelstyles() {
        return di_bpmnlabelstyles;
    }

    public void addDi_bpmnlabelstyle(Di_bpmnlabelstyle di_bpmnlabelstyle) {
        this.di_bpmnlabelstyles.add(di_bpmnlabelstyle);
    }
    public List<di_BPMNPlane> getDi_bpmnplanes() {
        return di_bpmnplanes;
    }

    public void addDi_bpmnplane(Di_bpmnplane di_bpmnplane) {
        this.di_bpmnplanes.add(di_bpmnplane);
    }
    public List<di_BPMNShape> getDi_bpmnshapes() {
        return di_bpmnshapes;
    }

    public void addDi_bpmnshape(Di_bpmnshape di_bpmnshape) {
        this.di_bpmnshapes.add(di_bpmnshape);
    }
    public List<di_BPMNLabel> getDi_bpmnlabels() {
        return di_bpmnlabels;
    }

    public void addDi_bpmnlabel(Di_bpmnlabel di_bpmnlabel) {
        this.di_bpmnlabels.add(di_bpmnlabel);
    }

}