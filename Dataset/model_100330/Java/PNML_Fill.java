





import java.util.List;
import java.util.ArrayList;

public class PNML_Fill  {

    private String gradientrotation;





    private AnnotationGraphics annotationgraphics;




    private URI uri;




    private EdgeGraphics edgegraphics;




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

    public AnnotationGraphics getAnnotationgraphics() {
        return annotationgraphics;
    }

    public void setAnnotationgraphics(AnnotationGraphics annotationgraphics) {
        this.annotationgraphics = annotationgraphics;
    }
    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }
    public EdgeGraphics getEdgegraphics() {
        return edgegraphics;
    }

    public void setEdgegraphics(EdgeGraphics edgegraphics) {
        this.edgegraphics = edgegraphics;
    }
    public NodeGraphics getNodegraphics() {
        return nodegraphics;
    }

    public void setNodegraphics(NodeGraphics nodegraphics) {
        this.nodegraphics = nodegraphics;
    }

}