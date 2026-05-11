





import java.util.List;
import java.util.ArrayList;

public class myDsl_voidType extends type_specifier {

    private String void_type;



    public myDsl_voidType(
        String void_type    ) {
        super(
        );
        this.void_type = void_type;
    }


    public String getVoid_type() {
        return void_type;
    }

    public void setVoid_type(String void_type) {
        this.void_type = void_type;
    }


}