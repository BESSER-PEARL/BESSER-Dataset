





import java.util.List;
import java.util.ArrayList;

public class di_BPMNDiagram extends Diagram {






    private di_DocumentRoot di_documentroot;




    private List<di_BPMNLabelStyle> di_bpmnlabelstyles;


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


    public di_DocumentRoot getDi_documentroot() {
        return di_documentroot;
    }

    public void setDi_documentroot(di_DocumentRoot di_documentroot) {
        this.di_documentroot = di_documentroot;
    }
    public List<di_BPMNLabelStyle> getDi_bpmnlabelstyles() {
        return di_bpmnlabelstyles;
    }

    public void addDi_bpmnlabelstyle(Di_bpmnlabelstyle di_bpmnlabelstyle) {
        this.di_bpmnlabelstyles.add(di_bpmnlabelstyle);
    }

}