





import java.util.List;
import java.util.ArrayList;

public class trnet_Operator  {

    private String id;





    private trnet_TrNetModel trnet_trnetmodel;


    public trnet_Operator(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public trnet_TrNetModel getTrnet_trnetmodel() {
        return trnet_trnetmodel;
    }

    public void setTrnet_trnetmodel(trnet_TrNetModel trnet_trnetmodel) {
        this.trnet_trnetmodel = trnet_trnetmodel;
    }

}