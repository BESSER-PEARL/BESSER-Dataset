





import java.util.List;
import java.util.ArrayList;

public class pascal_number  {

    private String integer;
    private String real;





    private pascal_constant pascal_constant;




    private pascal_factor pascal_factor;


    public pascal_number(
        String integer,        String real    ) {
        this.integer = integer;
        this.real = real;
    }


    public String getInteger() {
        return integer;
    }

    public void setInteger(String integer) {
        this.integer = integer;
    }
    public String getReal() {
        return real;
    }

    public void setReal(String real) {
        this.real = real;
    }

    public pascal_constant getPascal_constant() {
        return pascal_constant;
    }

    public void setPascal_constant(pascal_constant pascal_constant) {
        this.pascal_constant = pascal_constant;
    }
    public pascal_factor getPascal_factor() {
        return pascal_factor;
    }

    public void setPascal_factor(pascal_factor pascal_factor) {
        this.pascal_factor = pascal_factor;
    }

}