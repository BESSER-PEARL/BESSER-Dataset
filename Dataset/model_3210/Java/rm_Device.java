





import java.util.List;
import java.util.ArrayList;

public class rm_Device  {

    private int cacheSize;





    private rm_ResourceModel rm_resourcemodel;


    public rm_Device(
        int cacheSize    ) {
        this.cacheSize = cacheSize;
    }


    public int getCachesize() {
        return cacheSize;
    }

    public void setCachesize(int cacheSize) {
        this.cacheSize = cacheSize;
    }

    public rm_ResourceModel getRm_resourcemodel() {
        return rm_resourcemodel;
    }

    public void setRm_resourcemodel(rm_ResourceModel rm_resourcemodel) {
        this.rm_resourcemodel = rm_resourcemodel;
    }

}