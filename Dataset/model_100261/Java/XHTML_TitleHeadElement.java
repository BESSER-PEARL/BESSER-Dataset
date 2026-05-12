





import java.util.List;
import java.util.ArrayList;

public class XHTML_TitleHeadElement extends HeadElement {






    private List<HeadMisc> headmiscs;


    public XHTML_TitleHeadElement(
    ) {
        super(
        );
        this.headmiscs = new ArrayList<>();
    }

    public XHTML_TitleHeadElement(
        ArrayList<HeadMisc> headmiscs    ) {
        this.headmiscs = headmiscs;
    }


    public List<HeadMisc> getHeadmiscs() {
        return headmiscs;
    }

    public void addHeadmisc(Headmisc headmisc) {
        this.headmiscs.add(headmisc);
    }

}