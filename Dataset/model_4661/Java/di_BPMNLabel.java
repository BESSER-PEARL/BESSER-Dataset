





import java.util.List;
import java.util.ArrayList;

public class di_BPMNLabel extends Label {






    private di_BPMNEdge di_bpmnedge;




    private di_BPMNLabelStyle di_bpmnlabelstyle;




    private di_DocumentRoot di_documentroot;


    public di_BPMNLabel(
    ) {
        super(
        );
    }



    public di_BPMNEdge getDi_bpmnedge() {
        return di_bpmnedge;
    }

    public void setDi_bpmnedge(di_BPMNEdge di_bpmnedge) {
        this.di_bpmnedge = di_bpmnedge;
    }
    public di_BPMNLabelStyle getDi_bpmnlabelstyle() {
        return di_bpmnlabelstyle;
    }

    public void setDi_bpmnlabelstyle(di_BPMNLabelStyle di_bpmnlabelstyle) {
        this.di_bpmnlabelstyle = di_bpmnlabelstyle;
    }
    public di_DocumentRoot getDi_documentroot() {
        return di_documentroot;
    }

    public void setDi_documentroot(di_DocumentRoot di_documentroot) {
        this.di_documentroot = di_documentroot;
    }

}