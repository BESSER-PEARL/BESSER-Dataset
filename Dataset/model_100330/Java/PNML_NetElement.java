





import java.util.List;
import java.util.ArrayList;

public class PNML_NetElement extends IdedElement {






    private PNMLDocument pnmldocument;




    private List<NetContent> netcontents;




    private URI uri;


    public PNML_NetElement(
    ) {
        super(
        );
        this.netcontents = new ArrayList<>();
    }

    public PNML_NetElement(
        ArrayList<NetContent> netcontents    ) {
        this.netcontents = netcontents;
    }


    public PNMLDocument getPnmldocument() {
        return pnmldocument;
    }

    public void setPnmldocument(PNMLDocument pnmldocument) {
        this.pnmldocument = pnmldocument;
    }
    public List<NetContent> getNetcontents() {
        return netcontents;
    }

    public void addNetcontent(Netcontent netcontent) {
        this.netcontents.add(netcontent);
    }
    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }

}