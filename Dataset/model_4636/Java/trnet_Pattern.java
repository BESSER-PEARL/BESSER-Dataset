





import java.util.List;
import java.util.ArrayList;

public class trnet_Pattern  {

    private String id;
    private int expected_size;





    private trnet_TrNetModel trnet_trnetmodel;


    public trnet_Pattern(
        String id,        int expected_size    ) {
        this.id = id;
        this.expected_size = expected_size;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getExpected_size() {
        return expected_size;
    }

    public void setExpected_size(int expected_size) {
        this.expected_size = expected_size;
    }

    public trnet_TrNetModel getTrnet_trnetmodel() {
        return trnet_trnetmodel;
    }

    public void setTrnet_trnetmodel(trnet_TrNetModel trnet_trnetmodel) {
        this.trnet_trnetmodel = trnet_trnetmodel;
    }

}