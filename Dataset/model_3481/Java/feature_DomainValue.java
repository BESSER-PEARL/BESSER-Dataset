





import java.util.List;
import java.util.ArrayList;

public class feature_DomainValue  {

    private String name;
    private int int;





    private feature_DiscreteDomain feature_discretedomain;


    public feature_DomainValue(
        String name,        int int    ) {
        this.name = name;
        this.int = int;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getInt() {
        return int;
    }

    public void setInt(int int) {
        this.int = int;
    }

    public feature_DiscreteDomain getFeature_discretedomain() {
        return feature_discretedomain;
    }

    public void setFeature_discretedomain(feature_DiscreteDomain feature_discretedomain) {
        this.feature_discretedomain = feature_discretedomain;
    }

}