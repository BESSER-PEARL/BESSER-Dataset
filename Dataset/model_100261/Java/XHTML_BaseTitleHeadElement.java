





import java.util.List;
import java.util.ArrayList;

public class XHTML_BaseTitleHeadElement  {






    private List<HeadMisc> headmiscs;


    public XHTML_BaseTitleHeadElement(
    ) {
        this.headmiscs = new ArrayList<>();
    }

    public XHTML_BaseTitleHeadElement(
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