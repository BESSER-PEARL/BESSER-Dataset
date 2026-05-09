





import java.util.List;
import java.util.ArrayList;

public class myDsl_ReactServicesType  {

    private String name;





    private myDsl_ReactServicesRelation mydsl_reactservicesrelation;


    public myDsl_ReactServicesType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_ReactServicesRelation getMydsl_reactservicesrelation() {
        return mydsl_reactservicesrelation;
    }

    public void setMydsl_reactservicesrelation(myDsl_ReactServicesRelation mydsl_reactservicesrelation) {
        this.mydsl_reactservicesrelation = mydsl_reactservicesrelation;
    }

}