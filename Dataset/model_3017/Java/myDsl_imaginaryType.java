





import java.util.List;
import java.util.ArrayList;

public class myDsl_imaginaryType extends type_specifier {

    private String imaginary_type;



    public myDsl_imaginaryType(
        String imaginary_type    ) {
        super(
        );
        this.imaginary_type = imaginary_type;
    }


    public String getImaginary_type() {
        return imaginary_type;
    }

    public void setImaginary_type(String imaginary_type) {
        this.imaginary_type = imaginary_type;
    }


}