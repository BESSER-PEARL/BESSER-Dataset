





import java.util.List;
import java.util.ArrayList;

public class XHTML_TitleBaseHeadElement  {






    private Title title;




    private List<HeadMisc> headmiscs;


    public XHTML_TitleBaseHeadElement(
    ) {
        this.headmiscs = new ArrayList<>();
    }

    public XHTML_TitleBaseHeadElement(
        ArrayList<HeadMisc> headmiscs    ) {
        this.headmiscs = headmiscs;
    }


    public Title getTitle() {
        return title;
    }

    public void setTitle(Title title) {
        this.title = title;
    }
    public List<HeadMisc> getHeadmiscs() {
        return headmiscs;
    }

    public void addHeadmisc(Headmisc headmisc) {
        this.headmiscs.add(headmisc);
    }

}