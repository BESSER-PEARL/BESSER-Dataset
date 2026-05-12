





import java.util.List;
import java.util.ArrayList;

public class XHTML_BaseHeadElement extends HeadElement {






    private List<HeadMisc> headmiscs;


    public XHTML_BaseHeadElement(
    ) {
        super(
        );
        this.headmiscs = new ArrayList<>();
    }

    public XHTML_BaseHeadElement(
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