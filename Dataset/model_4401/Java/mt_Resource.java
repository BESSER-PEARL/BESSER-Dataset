





import java.util.List;
import java.util.ArrayList;

public class mt_Resource  {

    private String name;





    private mt_ResourceSet mt_resourceset;


    public mt_Resource(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mt_ResourceSet getMt_resourceset() {
        return mt_resourceset;
    }

    public void setMt_resourceset(mt_ResourceSet mt_resourceset) {
        this.mt_resourceset = mt_resourceset;
    }

}