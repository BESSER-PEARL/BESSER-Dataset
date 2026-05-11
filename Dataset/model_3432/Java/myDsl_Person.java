





import java.util.List;
import java.util.ArrayList;

public class myDsl_Person  {

    private String name;





    private myDsl_School mydsl_school;


    public myDsl_Person(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_School getMydsl_school() {
        return mydsl_school;
    }

    public void setMydsl_school(myDsl_School mydsl_school) {
        this.mydsl_school = mydsl_school;
    }

}