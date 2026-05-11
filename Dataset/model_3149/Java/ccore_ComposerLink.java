





import java.util.List;
import java.util.ArrayList;

public class ccore_ComposerLink  {






    private ccore_Composer ccore_composer;




    private List<ccore_Exporter> ccore_exporters;




    private ccore_LinkType ccore_linktype;


    public ccore_ComposerLink(
    ) {
        this.ccore_exporters = new ArrayList<>();
    }

    public ccore_ComposerLink(
        ArrayList<ccore_Exporter> ccore_exporters    ) {
        this.ccore_exporters = ccore_exporters;
    }


    public ccore_Composer getCcore_composer() {
        return ccore_composer;
    }

    public void setCcore_composer(ccore_Composer ccore_composer) {
        this.ccore_composer = ccore_composer;
    }
    public List<ccore_Exporter> getCcore_exporters() {
        return ccore_exporters;
    }

    public void addCcore_exporter(Ccore_exporter ccore_exporter) {
        this.ccore_exporters.add(ccore_exporter);
    }
    public ccore_LinkType getCcore_linktype() {
        return ccore_linktype;
    }

    public void setCcore_linktype(ccore_LinkType ccore_linktype) {
        this.ccore_linktype = ccore_linktype;
    }

}