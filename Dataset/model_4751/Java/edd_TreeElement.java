





import java.util.List;
import java.util.ArrayList;

public class edd_TreeElement  {

    private String index;
    private String name;





    private edd_EDD edd_edd;


    public edd_TreeElement(
        String index,        String name    ) {
        this.index = index;
        this.name = name;
    }


    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public edd_EDD getEdd_edd() {
        return edd_edd;
    }

    public void setEdd_edd(edd_EDD edd_edd) {
        this.edd_edd = edd_edd;
    }

}