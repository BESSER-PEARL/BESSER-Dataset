





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_SVGFigure extends RealFigure {

    private String documentURI;
    private boolean noCanvasWidth;
    private boolean noCanvasHeight;



    public gmf_all_gmfgraph_SVGFigure(
        String documentURI,        boolean noCanvasWidth,        boolean noCanvasHeight    ) {
        super(
        );
        this.documentURI = documentURI;
        this.noCanvasWidth = noCanvasWidth;
        this.noCanvasHeight = noCanvasHeight;
    }


    public String getDocumenturi() {
        return documentURI;
    }

    public void setDocumenturi(String documentURI) {
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


}