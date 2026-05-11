





import java.util.List;
import java.util.ArrayList;

public class mt_ResourceSet  {






    private List<mt_Resource> mt_resources;


    public mt_ResourceSet(
    ) {
        this.mt_resources = new ArrayList<>();
    }

    public mt_ResourceSet(
        ArrayList<mt_Resource> mt_resources    ) {
        this.mt_resources = mt_resources;
    }


    public List<mt_Resource> getMt_resources() {
        return mt_resources;
    }

    public void addMt_resource(Mt_resource mt_resource) {
        this.mt_resources.add(mt_resource);
    }

}