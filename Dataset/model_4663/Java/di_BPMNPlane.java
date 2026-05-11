





import java.util.List;
import java.util.ArrayList;

public class di_BPMNPlane extends Plane {






    private di_BPMNDiagram di_bpmndiagram;




    private di_DocumentRoot di_documentroot;


    public di_BPMNPlane(
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
    public di_DocumentRoot getDi_documentroot() {
        return di_documentroot;
    }

    public void setDi_documentroot(di_DocumentRoot di_documentroot) {
        this.di_documentroot = di_documentroot;
    }

}