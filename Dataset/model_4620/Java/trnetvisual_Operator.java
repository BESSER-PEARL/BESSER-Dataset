





import java.util.List;
import java.util.ArrayList;

public class trnetvisual_Operator  {

    private String id;





    private trnetvisual_TrNetModel trnetvisual_trnetmodel;


    public trnetvisual_Operator(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public trnetvisual_TrNetModel getTrnetvisual_trnetmodel() {
        return trnetvisual_trnetmodel;
    }

    public void setTrnetvisual_trnetmodel(trnetvisual_TrNetModel trnetvisual_trnetmodel) {
        this.trnetvisual_trnetmodel = trnetvisual_trnetmodel;
    }

}