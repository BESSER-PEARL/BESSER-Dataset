





import java.util.List;
import java.util.ArrayList;

public class trnetvisual_Pattern  {

    private float expected_size;
    private String id;





    private trnetvisual_TrNetModel trnetvisual_trnetmodel;


    public trnetvisual_Pattern(
        float expected_size,        String id    ) {
        this.expected_size = expected_size;
        this.id = id;
    }


    public float getExpected_size() {
        return expected_size;
    }

    public void setExpected_size(float expected_size) {
        this.expected_size = expected_size;
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