





import java.util.List;
import java.util.ArrayList;

public class sqlDSL_SEnumLiteral  {

    private String name;
    private int value;





    private sqlDSL_SEnum sqldsl_senum;


    public sqlDSL_SEnumLiteral(
        String name,        int value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public sqlDSL_SEnum getSqldsl_senum() {
        return sqldsl_senum;
    }

    public void setSqldsl_senum(sqlDSL_SEnum sqldsl_senum) {
        this.sqldsl_senum = sqldsl_senum;
    }

}