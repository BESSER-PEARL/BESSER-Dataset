





import java.util.List;
import java.util.ArrayList;

public class pascal_any_number  {

    private String real;
    private String integer;





    private pascal_number pascal_number;


    public pascal_any_number(
        String real,        String integer    ) {
        this.real = real;
        this.integer = integer;
    }


    public String getReal() {
        return real;
    }

    public void setReal(String real) {
        this.real = real;
    }
    public String getInteger() {
        return integer;
    }

    public void setInteger(String integer) {
        this.integer = integer;
    }

    public pascal_number getPascal_number() {
        return pascal_number;
    }

    public void setPascal_number(pascal_number pascal_number) {
        this.pascal_number = pascal_number;
    }

}