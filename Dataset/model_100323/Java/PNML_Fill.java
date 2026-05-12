





import java.util.List;
import java.util.ArrayList;

public class PNML_Fill  {

    private String gradientrotation;





    private NodeGraphics nodegraphics;


    public PNML_Fill(
        String gradientrotation    ) {
        this.gradientrotation = gradientrotation;
    }


    public String getGradientrotation() {
        return gradientrotation;
    }

    public void setGradientrotation(String gradientrotation) {
        this.gradientrotation = gradientrotation;
    }

    public NodeGraphics getNodegraphics() {
        return nodegraphics;
    }

    public void setNodegraphics(NodeGraphics nodegraphics) {
        this.nodegraphics = nodegraphics;
    }

}