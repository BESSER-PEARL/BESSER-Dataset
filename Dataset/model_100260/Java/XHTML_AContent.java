





import java.util.List;
import java.util.ArrayList;

public class XHTML_AContent  {






    private List<PCDATA> pcdatas;


    public XHTML_AContent(
    ) {
        this.pcdatas = new ArrayList<>();
    }

    public XHTML_AContent(
        ArrayList<PCDATA> pcdatas    ) {
        this.pcdatas = pcdatas;
    }


    public List<PCDATA> getPcdatas() {
        return pcdatas;
    }

    public void addPcdata(Pcdata pcdata) {
        this.pcdatas.add(pcdata);
    }

}