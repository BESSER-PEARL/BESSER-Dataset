





import java.util.List;
import java.util.ArrayList;

public class di_BaseElement  {






    private di_BPMNShape di_bpmnshape;




    private di_BPMNPlane di_bpmnplane;




    private di_BPMNEdge di_bpmnedge;


    public di_BaseElement(
    ) {
    }



    public di_BPMNShape getDi_bpmnshape() {
        return di_bpmnshape;
    }

    public void setDi_bpmnshape(di_BPMNShape di_bpmnshape) {
        this.di_bpmnshape = di_bpmnshape;
    }
    public di_BPMNPlane getDi_bpmnplane() {
        return di_bpmnplane;
    }

    public void setDi_bpmnplane(di_BPMNPlane di_bpmnplane) {
        this.di_bpmnplane = di_bpmnplane;
    }
    public di_BPMNEdge getDi_bpmnedge() {
        return di_bpmnedge;
    }

    public void setDi_bpmnedge(di_BPMNEdge di_bpmnedge) {
        this.di_bpmnedge = di_bpmnedge;
    }

}