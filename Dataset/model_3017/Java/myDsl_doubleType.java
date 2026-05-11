





import java.util.List;
import java.util.ArrayList;

public class myDsl_doubleType extends type_specifier {

    private String double_type;



    public myDsl_doubleType(
        String double_type    ) {
        super(
        );
        this.double_type = double_type;
    }


    public String getDouble_type() {
        return double_type;
    }

    public void setDouble_type(String double_type) {
        this.double_type = double_type;
    }


}