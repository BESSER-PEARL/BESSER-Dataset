





import java.util.List;
import java.util.ArrayList;

public class soa_Comment  {

    private String value;





    private soa_Feature soa_feature;


    public soa_Comment(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public soa_Feature getSoa_feature() {
        return soa_feature;
    }

    public void setSoa_feature(soa_Feature soa_feature) {
        this.soa_feature = soa_feature;
    }

}