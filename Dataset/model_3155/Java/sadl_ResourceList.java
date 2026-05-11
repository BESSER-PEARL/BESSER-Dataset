





import java.util.List;
import java.util.ArrayList;

public class sadl_ResourceList  {






    private List<sadl_ResourceName> sadl_resourcenames;


    public sadl_ResourceList(
    ) {
        this.sadl_resourcenames = new ArrayList<>();
    }

    public sadl_ResourceList(
        ArrayList<sadl_ResourceName> sadl_resourcenames    ) {
        this.sadl_resourcenames = sadl_resourcenames;
    }


    public List<sadl_ResourceName> getSadl_resourcenames() {
        return sadl_resourcenames;
    }

    public void addSadl_resourcename(Sadl_resourcename sadl_resourcename) {
        this.sadl_resourcenames.add(sadl_resourcename);
    }

}