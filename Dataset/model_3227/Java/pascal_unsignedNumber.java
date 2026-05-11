





import java.util.List;
import java.util.ArrayList;

public class pascal_unsignedNumber  {

    private String unsignedReal;





    private pascal_unsignedConstant pascal_unsignedconstant;




    private pascal_constant pascal_constant;


    public pascal_unsignedNumber(
        String unsignedReal    ) {
        this.unsignedReal = unsignedReal;
    }


    public String getUnsignedreal() {
        return unsignedReal;
    }

    public void setUnsignedreal(String unsignedReal) {
        this.unsignedReal = unsignedReal;
    }

    public pascal_unsignedConstant getPascal_unsignedconstant() {
        return pascal_unsignedconstant;
    }

    public void setPascal_unsignedconstant(pascal_unsignedConstant pascal_unsignedconstant) {
        this.pascal_unsignedconstant = pascal_unsignedconstant;
    }
    public pascal_constant getPascal_constant() {
        return pascal_constant;
    }

    public void setPascal_constant(pascal_constant pascal_constant) {
        this.pascal_constant = pascal_constant;
    }

}