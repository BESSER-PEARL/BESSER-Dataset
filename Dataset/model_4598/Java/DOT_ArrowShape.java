





import java.util.List;
import java.util.ArrayList;

public class DOT_ArrowShape extends Shape {

    private String clipping;
    private int size;
    private boolean isPlain;





    private DOT_DirectedArc dot_directedarc;




    private DOT_DirectedArc dot_directedarc;


    public DOT_ArrowShape(
        String clipping,        int size,        boolean isPlain    ) {
        super(
        );
        this.clipping = clipping;
        this.size = size;
        this.isPlain = isPlain;
    }


    public String getClipping() {
        return clipping;
    }

    public void setClipping(String clipping) {
        this.clipping = clipping;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public boolean getIsplain() {
        return isPlain;
    }

    public void setIsplain(boolean isPlain) {
        this.isPlain = isPlain;
    }

    public DOT_DirectedArc getDot_directedarc() {
        return dot_directedarc;
    }

    public void setDot_directedarc(DOT_DirectedArc dot_directedarc) {
        this.dot_directedarc = dot_directedarc;
    }
    public DOT_DirectedArc getDot_directedarc() {
        return dot_directedarc;
    }

    public void setDot_directedarc(DOT_DirectedArc dot_directedarc) {
        this.dot_directedarc = dot_directedarc;
    }

}