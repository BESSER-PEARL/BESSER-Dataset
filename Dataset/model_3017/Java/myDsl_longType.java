





import java.util.List;
import java.util.ArrayList;

public class myDsl_longType extends type_specifier {

    private String long_type;



    public myDsl_longType(
        String long_type    ) {
        super(
        );
        this.long_type = long_type;
    }


    public String getLong_type() {
        return long_type;
    }

    public void setLong_type(String long_type) {
        this.long_type = long_type;
    }


}