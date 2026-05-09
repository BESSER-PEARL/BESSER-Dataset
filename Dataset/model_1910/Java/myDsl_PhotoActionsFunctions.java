





import java.util.List;
import java.util.ArrayList;

public class myDsl_PhotoActionsFunctions  {

    private String name;





    private myDsl_PhotoActions mydsl_photoactions;


    public myDsl_PhotoActionsFunctions(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_PhotoActions getMydsl_photoactions() {
        return mydsl_photoactions;
    }

    public void setMydsl_photoactions(myDsl_PhotoActions mydsl_photoactions) {
        this.mydsl_photoactions = mydsl_photoactions;
    }

}