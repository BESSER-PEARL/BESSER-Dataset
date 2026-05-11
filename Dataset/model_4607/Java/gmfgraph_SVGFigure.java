





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_SVGFigure extends RealFigure {

    private String documentURI;
    private boolean noCanvasHeight;
    private boolean noCanvasWidth;



    public gmfgraph_SVGFigure(
        String documentURI,        boolean noCanvasHeight,        boolean noCanvasWidth    ) {
        super(
        );
        this.documentURI = documentURI;
        this.noCanvasHeight = noCanvasHeight;
        this.noCanvasWidth = noCanvasWidth;
    }


    public String getDocumenturi() {
        return documentURI;
    }

    public void setDocumenturi(String documentURI) {
        this.documentURI = documentURI;
    }
    public boolean getNocanvasheight() {
        return noCanvasHeight;
    }

    public void setNocanvasheight(boolean noCanvasHeight) {
        this.noCanvasHeight = noCanvasHeight;
    }
    public boolean getNocanvaswidth() {
        return noCanvasWidth;
    }

    public void setNocanvaswidth(boolean noCanvasWidth) {
        this.noCanvasWidth = noCanvasWidth;
    }


}