





import java.util.List;
import java.util.ArrayList;

public class xdoc_Part extends AbstractSection {






    private List<xdoc_Chapter> xdoc_chapters;




    private xdoc_Document xdoc_document;


    public xdoc_Part(
    ) {
        super(
        );
        this.xdoc_chapters = new ArrayList<>();
    }

    public xdoc_Part(
        ArrayList<xdoc_Chapter> xdoc_chapters    ) {
        this.xdoc_chapters = xdoc_chapters;
    }


    public List<xdoc_Chapter> getXdoc_chapters() {
        return xdoc_chapters;
    }

    public void addXdoc_chapter(Xdoc_chapter xdoc_chapter) {
        this.xdoc_chapters.add(xdoc_chapter);
    }
    public xdoc_Document getXdoc_document() {
        return xdoc_document;
    }

    public void setXdoc_document(xdoc_Document xdoc_document) {
        this.xdoc_document = xdoc_document;
    }

}