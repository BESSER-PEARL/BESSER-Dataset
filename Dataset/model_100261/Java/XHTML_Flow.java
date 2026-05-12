





import java.util.List;
import java.util.ArrayList;

public class XHTML_Flow  {






    private List<PCDATA> pcdatas;


    public XHTML_Flow(
    ) {
        this.pcdatas = new ArrayList<>();
    }

    public XHTML_Flow(
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