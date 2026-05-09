





import java.util.List;
import java.util.ArrayList;

public class myDsl_BusinessLogicSegments  {

    private String name;





    private myDsl_BusinessLogicContent mydsl_businesslogiccontent;


    public myDsl_BusinessLogicSegments(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_BusinessLogicContent getMydsl_businesslogiccontent() {
        return mydsl_businesslogiccontent;
    }

    public void setMydsl_businesslogiccontent(myDsl_BusinessLogicContent mydsl_businesslogiccontent) {
        this.mydsl_businesslogiccontent = mydsl_businesslogiccontent;
    }

}