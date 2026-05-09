





import java.util.List;
import java.util.ArrayList;

public class docbook_ImageData  {

    private String fileref;
    private String depth;
    private String width;





    private docbook_ImageObject docbook_imageobject;




    private docbook_ImageObject docbook_imageobject;


    public docbook_ImageData(
        String fileref,        String depth,        String width    ) {
        this.fileref = fileref;
        this.depth = depth;
        this.width = width;
    }


    public String getFileref() {
        return fileref;
    }

    public void setFileref(String fileref) {
        this.fileref = fileref;
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

    public docbook_ImageObject getDocbook_imageobject() {
        return docbook_imageobject;
    }

    public void setDocbook_imageobject(docbook_ImageObject docbook_imageobject) {
        this.docbook_imageobject = docbook_imageobject;
    }
    public docbook_ImageObject getDocbook_imageobject() {
        return docbook_imageobject;
    }

    public void setDocbook_imageobject(docbook_ImageObject docbook_imageobject) {
        this.docbook_imageobject = docbook_imageobject;
    }

}