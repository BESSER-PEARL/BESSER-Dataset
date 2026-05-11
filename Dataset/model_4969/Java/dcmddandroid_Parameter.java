





import java.util.List;
import java.util.ArrayList;

public class dcmddandroid_Parameter extends NamedElement {

    private String type;





    private dcmddandroid_Method dcmddandroid_method;


    public dcmddandroid_Parameter(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public dcmddandroid_Method getDcmddandroid_method() {
        return dcmddandroid_method;
    }

    public void setDcmddandroid_method(dcmddandroid_Method dcmddandroid_method) {
        this.dcmddandroid_method = dcmddandroid_method;
    }

}