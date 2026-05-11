





import java.util.List;
import java.util.ArrayList;

public class krendering_KRendering extends KStyleHolder, KGraphData {






    private krendering_KPolyline krendering_kpolyline;




    private krendering_KPlacementData krendering_kplacementdata;




    private List<krendering_KAction> krendering_kactions;




    private krendering_KImage krendering_kimage;


    public krendering_KRendering(
    ) {
        super(
        );
        this.krendering_kactions = new ArrayList<>();
    }

    public krendering_KRendering(
        ArrayList<krendering_KAction> krendering_kactions    ) {
        this.krendering_kactions = krendering_kactions;
    }


    public krendering_KPolyline getKrendering_kpolyline() {
        return krendering_kpolyline;
    }

    public void setKrendering_kpolyline(krendering_KPolyline krendering_kpolyline) {
        this.krendering_kpolyline = krendering_kpolyline;
    }
    public krendering_KPlacementData getKrendering_kplacementdata() {
        return krendering_kplacementdata;
    }

    public void setKrendering_kplacementdata(krendering_KPlacementData krendering_kplacementdata) {
        this.krendering_kplacementdata = krendering_kplacementdata;
    }
    public List<krendering_KAction> getKrendering_kactions() {
        return krendering_kactions;
    }

    public void addKrendering_kaction(Krendering_kaction krendering_kaction) {
        this.krendering_kactions.add(krendering_kaction);
    }
    public krendering_KImage getKrendering_kimage() {
        return krendering_kimage;
    }

    public void setKrendering_kimage(krendering_KImage krendering_kimage) {
        this.krendering_kimage = krendering_kimage;
    }

}