





import java.util.List;
import java.util.ArrayList;

public class diagraph_DLineEdge extends DSimpleEdge {

    private String arrows;



    public diagraph_DLineEdge(
        String arrows    ) {
        super(
        );
        this.arrows = arrows;
    }


    public String getArrows() {
        return arrows;
    }

    public void setArrows(String arrows) {
        this.arrows = arrows;
    }


}