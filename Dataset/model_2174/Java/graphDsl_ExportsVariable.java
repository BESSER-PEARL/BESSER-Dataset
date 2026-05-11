





import java.util.List;
import java.util.ArrayList;

public class graphDsl_ExportsVariable  {

    private String name;
    private int intValue;
    private String strValue;



    public graphDsl_ExportsVariable(
        String name,        int intValue,        String strValue    ) {
        this.name = name;
        this.intValue = intValue;
        this.strValue = strValue;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getIntvalue() {
        return intValue;
    }

    public void setIntvalue(int intValue) {
        this.intValue = intValue;
    }
    public String getStrvalue() {
        return strValue;
    }

    public void setStrvalue(String strValue) {
        this.strValue = strValue;
    }


}