





import java.util.List;
import java.util.ArrayList;

public class ansic_constant  {

    private String char;
    private String f_constant;
    private int i_constant;
    private String enumz;



    public ansic_constant(
        String char,        String f_constant,        int i_constant,        String enumz    ) {
        this.char = char;
        this.f_constant = f_constant;
        this.i_constant = i_constant;
        this.enumz = enumz;
    }


    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }
    public String getF_constant() {
        return f_constant;
    }

    public void setF_constant(String f_constant) {
        this.f_constant = f_constant;
    }
    public int getI_constant() {
        return i_constant;
    }

    public void setI_constant(int i_constant) {
        this.i_constant = i_constant;
    }
    public String getEnumz() {
        return enumz;
    }

    public void setEnumz(String enumz) {
        this.enumz = enumz;
    }


}