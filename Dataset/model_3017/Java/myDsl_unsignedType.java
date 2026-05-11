





import java.util.List;
import java.util.ArrayList;

public class myDsl_unsignedType extends type_specifier {

    private String unsigned_type;



    public myDsl_unsignedType(
        String unsigned_type    ) {
        super(
        );
        this.unsigned_type = unsigned_type;
    }


    public String getUnsigned_type() {
        return unsigned_type;
    }

    public void setUnsigned_type(String unsigned_type) {
        this.unsigned_type = unsigned_type;
    }


}