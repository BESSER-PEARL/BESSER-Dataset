





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_SVGFigure extends RealFigure {

    private boolean noCanvasWidth;
    private boolean noCanvasHeight;
    private String documentURI;



    public gmfgraph_SVGFigure(
        boolean noCanvasWidth,        boolean noCanvasHeight,        String documentURI    ) {
        super(
        );
        this.noCanvasWidth = noCanvasWidth;
        this.noCanvasHeight = noCanvasHeight;
        this.documentURI = documentURI;
    }


    public boolean getNocanvaswidth() {
        return noCanvasWidth;
    }

    public void setNocanvaswidth(boolean noCanvasWidth) {
        this.noCanvasWidth = noCanvasWidth;
    }
    public boolean getNocanvasheight() {
        return noCanvasHeight;
    }

    public void setNocanvasheight(boolean noCanvasHeight) {
        this.noCanvasHeight = noCanvasHeight;
    }
    public String getDocumenturi() {
        return documentURI;
    }

    public void setDocumenturi(String documentURI) {
        this.documentURI = documentURI;
    }


}