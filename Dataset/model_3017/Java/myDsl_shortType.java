





import java.util.List;
import java.util.ArrayList;

public class myDsl_shortType extends type_specifier {

    private String short_type;



    public myDsl_shortType(
        String short_type    ) {
        super(
        );
        this.short_type = short_type;
    }


    public String getShort_type() {
        return short_type;
    }

    public void setShort_type(String short_type) {
        this.short_type = short_type;
    }


}