





import java.util.List;
import java.util.ArrayList;

public class myDsl_Library  {

    private String name;
    private String isNative;





    private myDsl_Subproject mydsl_subproject;


    public myDsl_Library(
        String name,        String isNative    ) {
        this.name = name;
        this.isNative = isNative;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsnative() {
        return isNative;
    }

    public void setIsnative(String isNative) {
        this.isNative = isNative;
    }

    public myDsl_Subproject getMydsl_subproject() {
        return mydsl_subproject;
    }

    public void setMydsl_subproject(myDsl_Subproject mydsl_subproject) {
        this.mydsl_subproject = mydsl_subproject;
    }

}