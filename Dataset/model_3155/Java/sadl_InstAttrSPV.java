





import java.util.List;
import java.util.ArrayList;

public class sadl_InstAttrSPV extends GraphPattern {






    private List<sadl_ResourceByName> sadl_resourcebynames;




    private sadl_ResourceByName sadl_resourcebyname;


    public sadl_InstAttrSPV(
    ) {
        super(
        );
        this.sadl_resourcebynames = new ArrayList<>();
    }

    public sadl_InstAttrSPV(
        ArrayList<sadl_ResourceByName> sadl_resourcebynames    ) {
        this.sadl_resourcebynames = sadl_resourcebynames;
    }


    public List<sadl_ResourceByName> getSadl_resourcebynames() {
        return sadl_resourcebynames;
    }

    public void addSadl_resourcebyname(Sadl_resourcebyname sadl_resourcebyname) {
        this.sadl_resourcebynames.add(sadl_resourcebyname);
    }
    public sadl_ResourceByName getSadl_resourcebyname() {
        return sadl_resourcebyname;
    }

    public void setSadl_resourcebyname(sadl_ResourceByName sadl_resourcebyname) {
        this.sadl_resourcebyname = sadl_resourcebyname;
    }

}