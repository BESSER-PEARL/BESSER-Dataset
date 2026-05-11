





import java.util.List;
import java.util.ArrayList;

public class sxfm_Group extends CardinalizedElement {

    private String id;





    private sxfm_Feature sxfm_feature;


    public sxfm_Group(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public sxfm_Feature getSxfm_feature() {
        return sxfm_feature;
    }

    public void setSxfm_feature(sxfm_Feature sxfm_feature) {
        this.sxfm_feature = sxfm_feature;
    }

}