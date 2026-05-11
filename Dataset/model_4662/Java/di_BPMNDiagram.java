





import java.util.List;
import java.util.ArrayList;

public class di_BPMNDiagram extends Diagram {






    private List<di_BPMNLabelStyle> di_bpmnlabelstyles;




    private di_BPMNPlane di_bpmnplane;




    private di_DocumentRoot di_documentroot;


    public di_BPMNDiagram(
    ) {
        super(
        );
        this.di_bpmnlabelstyles = new ArrayList<>();
    }

    public di_BPMNDiagram(
        ArrayList<di_BPMNLabelStyle> di_bpmnlabelstyles    ) {
        this.di_bpmnlabelstyles = di_bpmnlabelstyles;
    }


    public List<di_BPMNLabelStyle> getDi_bpmnlabelstyles() {
        return di_bpmnlabelstyles;
    }

    public void addDi_bpmnlabelstyle(Di_bpmnlabelstyle di_bpmnlabelstyle) {
        this.di_bpmnlabelstyles.add(di_bpmnlabelstyle);
    }
    public di_BPMNPlane getDi_bpmnplane() {
        return di_bpmnplane;
    }

    public void setDi_bpmnplane(di_BPMNPlane di_bpmnplane) {
        this.di_bpmnplane = di_bpmnplane;
    }
    public di_DocumentRoot getDi_documentroot() {
        return di_documentroot;
    }

    public void setDi_documentroot(di_DocumentRoot di_documentroot) {
        this.di_documentroot = di_documentroot;
    }

}