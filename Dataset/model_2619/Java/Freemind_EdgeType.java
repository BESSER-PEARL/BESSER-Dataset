





import java.util.List;
import java.util.ArrayList;

public class Freemind_EdgeType  {

    private String Color;
    private String Width;
    private String Style;





    private Freemind_NodeType freemind_nodetype;




    private Freemind_DocumentRoot freemind_documentroot;


    public Freemind_EdgeType(
        String Color,        String Width,        String Style    ) {
        this.Color = Color;
        this.Width = Width;
        this.Style = Style;
    }


    public String getColor() {
        return Color;
    }

    public void setColor(String Color) {
        this.Color = Color;
    }
    public String getWidth() {
        return Width;
    }

    public void setWidth(String Width) {
        this.Width = Width;
    }
    public String getStyle() {
        return Style;
    }

    public void setStyle(String Style) {
        this.Style = Style;
    }

    public Freemind_NodeType getFreemind_nodetype() {
        return freemind_nodetype;
    }

    public void setFreemind_nodetype(Freemind_NodeType freemind_nodetype) {
        this.freemind_nodetype = freemind_nodetype;
    }
    public Freemind_DocumentRoot getFreemind_documentroot() {
        return freemind_documentroot;
    }

    public void setFreemind_documentroot(Freemind_DocumentRoot freemind_documentroot) {
        this.freemind_documentroot = freemind_documentroot;
    }

}