





import java.util.List;
import java.util.ArrayList;

public class di_BPMNLabelStyle extends Style {






    private di_BPMNDiagram di_bpmndiagram;




    private di_BPMNLabel di_bpmnlabel;




    private di_DocumentRoot di_documentroot;


    public di_BPMNLabelStyle(
    ) {
        super(
        );
    }



    public di_BPMNDiagram getDi_bpmndiagram() {
        return di_bpmndiagram;
    }

    public void setDi_bpmndiagram(di_BPMNDiagram di_bpmndiagram) {
        this.di_bpmndiagram = di_bpmndiagram;
    }
    public di_BPMNLabel getDi_bpmnlabel() {
        return di_bpmnlabel;
    }

    public void setDi_bpmnlabel(di_BPMNLabel di_bpmnlabel) {
        this.di_bpmnlabel = di_bpmnlabel;
    }
    public di_DocumentRoot getDi_documentroot() {
        return di_documentroot;
    }

    public void setDi_documentroot(di_DocumentRoot di_documentroot) {
        this.di_documentroot = di_documentroot;
    }

}