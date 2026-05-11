





import java.util.List;
import java.util.ArrayList;

public class rm_Memory  {

    private int size;





    private rm_ResourceModel rm_resourcemodel;


    public rm_Memory(
        int size    ) {
        this.size = size;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public rm_ResourceModel getRm_resourcemodel() {
        return rm_resourcemodel;
    }

    public void setRm_resourcemodel(rm_ResourceModel rm_resourcemodel) {
        this.rm_resourcemodel = rm_resourcemodel;
    }

}