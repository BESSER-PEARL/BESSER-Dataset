





import java.util.List;
import java.util.ArrayList;

public class myDsl_School  {

    private String name;





    private myDsl_SchoolModel mydsl_schoolmodel;


    public myDsl_School(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_SchoolModel getMydsl_schoolmodel() {
        return mydsl_schoolmodel;
    }

    public void setMydsl_schoolmodel(myDsl_SchoolModel mydsl_schoolmodel) {
        this.mydsl_schoolmodel = mydsl_schoolmodel;
    }

}