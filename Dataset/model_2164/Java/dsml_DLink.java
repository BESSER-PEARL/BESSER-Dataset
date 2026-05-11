





import java.util.List;
import java.util.ArrayList;

public class dsml_DLink extends DContainedEdge, DClassElement {






    private List<dsml_DLabel> dsml_dlabels;


    public dsml_DLink(
    ) {
        super(
        );
        this.dsml_dlabels = new ArrayList<>();
    }

    public dsml_DLink(
        ArrayList<dsml_DLabel> dsml_dlabels    ) {
        this.dsml_dlabels = dsml_dlabels;
    }


    public List<dsml_DLabel> getDsml_dlabels() {
        return dsml_dlabels;
    }

    public void addDsml_dlabel(Dsml_dlabel dsml_dlabel) {
        this.dsml_dlabels.add(dsml_dlabel);
    }

}