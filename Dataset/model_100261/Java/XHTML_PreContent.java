





import java.util.List;
import java.util.ArrayList;

public class XHTML_PreContent  {






    private List<PCDATA> pcdatas;


    public XHTML_PreContent(
    ) {
        this.pcdatas = new ArrayList<>();
    }

    public XHTML_PreContent(
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