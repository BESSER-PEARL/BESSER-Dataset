





import java.util.List;
import java.util.ArrayList;

public class myDsl_Eclass  {

    private String name;





    private myDsl_Epackage mydsl_epackage;


    public myDsl_Eclass(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Epackage getMydsl_epackage() {
        return mydsl_epackage;
    }

    public void setMydsl_epackage(myDsl_Epackage mydsl_epackage) {
        this.mydsl_epackage = mydsl_epackage;
    }

}