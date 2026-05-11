





import java.util.List;
import java.util.ArrayList;

public class cs_CSElement extends ENamedElement {

    private String maxZoom;
    private boolean resizable;
    private boolean templateRoot;
    private String selectable;
    private boolean draggable;
    private String minZoom;





    private cs_CSElement cs_cselement;




    private List<cs_CSElement> cs_cselements;


    public cs_CSElement(
        String maxZoom,        boolean resizable,        boolean templateRoot,        String selectable,        boolean draggable,        String minZoom    ) {
        super(
        );
        this.maxZoom = maxZoom;
        this.resizable = resizable;
        this.templateRoot = templateRoot;
        this.selectable = selectable;
        this.draggable = draggable;
        this.minZoom = minZoom;
        this.cs_cselements = new ArrayList<>();
    }

    public cs_CSElement(
        String maxZoom,        boolean resizable,        boolean templateRoot,        String selectable,        boolean draggable,        String minZoom        ArrayList<cs_CSElement> cs_cselements    ) {
        this.maxZoom = maxZoom;
        this.resizable = resizable;
        this.templateRoot = templateRoot;
        this.selectable = selectable;
        this.draggable = draggable;
        this.minZoom = minZoom;
        this.cs_cselements = cs_cselements;
    }

    public String getMaxzoom() {
        return maxZoom;
    }

    public void setMaxzoom(String maxZoom) {
        this.maxZoom = maxZoom;
    }
    public boolean getResizable() {
        return resizable;
    }

    public void setResizable(boolean resizable) {
        this.resizable = resizable;
    }
    public boolean getTemplateroot() {
        return templateRoot;
    }

    public void setTemplateroot(boolean templateRoot) {
        this.templateRoot = templateRoot;
    }
    public String getSelectable() {
        return selectable;
    }

    public void setSelectable(String selectable) {
        this.selectable = selectable;
    }
    public boolean getDraggable() {
        return draggable;
    }

    public void setDraggable(boolean draggable) {
        this.draggable = draggable;
    }
    public String getMinzoom() {
        return minZoom;
    }

    public void setMinzoom(String minZoom) {
        this.minZoom = minZoom;
    }

    public cs_CSElement getCs_cselement() {
        return cs_cselement;
    }

    public void setCs_cselement(cs_CSElement cs_cselement) {
        this.cs_cselement = cs_cselement;
    }
    public List<cs_CSElement> getCs_cselements() {
        return cs_cselements;
    }

    public void addCs_cselement(Cs_cselement cs_cselement) {
        this.cs_cselements.add(cs_cselement);
    }

}