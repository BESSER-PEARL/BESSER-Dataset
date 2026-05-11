





import java.util.List;
import java.util.ArrayList;

public class myDsl_complexType extends type_specifier {

    private String complex_type;



    public myDsl_complexType(
        String complex_type    ) {
        super(
        );
        this.complex_type = complex_type;
    }


    public String getComplex_type() {
        return complex_type;
    }

    public void setComplex_type(String complex_type) {
        this.complex_type = complex_type;
    }


}