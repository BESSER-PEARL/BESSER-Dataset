





import java.util.List;
import java.util.ArrayList;

public class Docbook_ImagedataType  {

    private String depth;
    private String width;
    private String align;
    private String fileref;
    private String scale;





    private Docbook_DocumentRoot docbook_documentroot;


    public Docbook_ImagedataType(
        String depth,        String width,        String align,        String fileref,        String scale    ) {
        this.depth = depth;
        this.width = width;
        this.align = align;
        this.fileref = fileref;
        this.scale = scale;
    }


    public String getDepth() {
        return depth;
    }

    public void setDepth(String depth) {
        this.depth = depth;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getFileref() {
        return fileref;
    }

    public void setFileref(String fileref) {
        this.fileref = fileref;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }

    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }

}