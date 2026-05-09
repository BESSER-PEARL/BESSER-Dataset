





import java.util.List;
import java.util.ArrayList;

public class myDsl_ReactInformation  {

    private String name;





    private myDsl_ReactInfo mydsl_reactinfo;


    public myDsl_ReactInformation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_ReactInfo getMydsl_reactinfo() {
        return mydsl_reactinfo;
    }

    public void setMydsl_reactinfo(myDsl_ReactInfo mydsl_reactinfo) {
        this.mydsl_reactinfo = mydsl_reactinfo;
    }

}