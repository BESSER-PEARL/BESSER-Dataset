





import java.util.List;
import java.util.ArrayList;

public class myDsl_signedType extends type_specifier {

    private String signed_type;



    public myDsl_signedType(
        String signed_type    ) {
        super(
        );
        this.signed_type = signed_type;
    }


    public String getSigned_type() {
        return signed_type;
    }

    public void setSigned_type(String signed_type) {
        this.signed_type = signed_type;
    }


}