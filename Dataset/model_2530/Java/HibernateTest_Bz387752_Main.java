





import java.util.List;
import java.util.ArrayList;

public class HibernateTest_Bz387752_Main  {

    private String strSettable;
    private String enumSettable;
    private String strUnsettable;
    private String enumUnsettable;



    public HibernateTest_Bz387752_Main(
        String strSettable,        String enumSettable,        String strUnsettable,        String enumUnsettable    ) {
        this.strSettable = strSettable;
        this.enumSettable = enumSettable;
        this.strUnsettable = strUnsettable;
        this.enumUnsettable = enumUnsettable;
    }


    public String getStrsettable() {
        return strSettable;
    }

    public void setStrsettable(String strSettable) {
        this.strSettable = strSettable;
    }
    public String getEnumsettable() {
        return enumSettable;
    }

    public void setEnumsettable(String enumSettable) {
        this.enumSettable = enumSettable;
    }
    public String getStrunsettable() {
        return strUnsettable;
    }

    public void setStrunsettable(String strUnsettable) {
        this.strUnsettable = strUnsettable;
    }
    public String getEnumunsettable() {
        return enumUnsettable;
    }

    public void setEnumunsettable(String enumUnsettable) {
        this.enumUnsettable = enumUnsettable;
    }


}