





import java.util.List;
import java.util.ArrayList;

public class myDsl_ReactServicesRelation  {

    private String name;





    private myDsl_ReactActionsContent mydsl_reactactionscontent;


    public myDsl_ReactServicesRelation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_ReactActionsContent getMydsl_reactactionscontent() {
        return mydsl_reactactionscontent;
    }

    public void setMydsl_reactactionscontent(myDsl_ReactActionsContent mydsl_reactactionscontent) {
        this.mydsl_reactactionscontent = mydsl_reactactionscontent;
    }

}