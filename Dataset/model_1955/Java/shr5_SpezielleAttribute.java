





import java.util.List;
import java.util.ArrayList;

public class shr5_SpezielleAttribute extends ModifikatorAttribute {

    private int edgeBasis;
    private int essenz;
    private int initativWuerfel;
    private int initative;
    private int ausweichen;
    private int edge;



    public shr5_SpezielleAttribute(
        int edgeBasis,        int essenz,        int initativWuerfel,        int initative,        int ausweichen,        int edge    ) {
        super(
        );
        this.edgeBasis = edgeBasis;
        this.essenz = essenz;
        this.initativWuerfel = initativWuerfel;
        this.initative = initative;
        this.ausweichen = ausweichen;
        this.edge = edge;
    }


    public int getEdgebasis() {
        return edgeBasis;
    }

    public void setEdgebasis(int edgeBasis) {
        this.edgeBasis = edgeBasis;
    }
    public int getEssenz() {
        return essenz;
    }

    public void setEssenz(int essenz) {
        this.essenz = essenz;
    }
    public int getInitativwuerfel() {
        return initativWuerfel;
    }

    public void setInitativwuerfel(int initativWuerfel) {
        this.initativWuerfel = initativWuerfel;
    }
    public int getInitative() {
        return initative;
    }

    public void setInitative(int initative) {
        this.initative = initative;
    }
    public int getAusweichen() {
        return ausweichen;
    }

    public void setAusweichen(int ausweichen) {
        this.ausweichen = ausweichen;
    }
    public int getEdge() {
        return edge;
    }

    public void setEdge(int edge) {
        this.edge = edge;
    }


}