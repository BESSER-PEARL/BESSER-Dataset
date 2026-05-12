





import java.util.List;
import java.util.ArrayList;

public class zhu_Region  {

    private String name;





    private zhu_TopRegion zhu_topregion;




    private zhu_States zhu_states;




    private List<zhu_Region> zhu_regions;


    public zhu_Region(
        String name    ) {
        this.name = name;
        this.zhu_regions = new ArrayList<>();
    }

    public zhu_Region(
        String name        ArrayList<zhu_Region> zhu_regions    ) {
        this.name = name;
        this.zhu_regions = zhu_regions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public zhu_TopRegion getZhu_topregion() {
        return zhu_topregion;
    }

    public void setZhu_topregion(zhu_TopRegion zhu_topregion) {
        this.zhu_topregion = zhu_topregion;
    }
    public zhu_States getZhu_states() {
        return zhu_states;
    }

    public void setZhu_states(zhu_States zhu_states) {
        this.zhu_states = zhu_states;
    }
    public List<zhu_Region> getZhu_regions() {
        return zhu_regions;
    }

    public void addZhu_region(Zhu_region zhu_region) {
        this.zhu_regions.add(zhu_region);
    }

}