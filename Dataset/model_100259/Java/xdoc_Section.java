





import java.util.List;
import java.util.ArrayList;

public class xdoc_Section extends AbstractSection {






    private xdoc_Chapter xdoc_chapter;




    private List<xdoc_Section2> xdoc_section2s;


    public xdoc_Section(
    ) {
        super(
        );
        this.xdoc_section2s = new ArrayList<>();
    }

    public xdoc_Section(
        ArrayList<xdoc_Section2> xdoc_section2s    ) {
        this.xdoc_section2s = xdoc_section2s;
    }


    public xdoc_Chapter getXdoc_chapter() {
        return xdoc_chapter;
    }

    public void setXdoc_chapter(xdoc_Chapter xdoc_chapter) {
        this.xdoc_chapter = xdoc_chapter;
    }
    public List<xdoc_Section2> getXdoc_section2s() {
        return xdoc_section2s;
    }

    public void addXdoc_section2(Xdoc_section2 xdoc_section2) {
        this.xdoc_section2s.add(xdoc_section2);
    }

}