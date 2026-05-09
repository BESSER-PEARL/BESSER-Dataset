





import java.util.List;
import java.util.ArrayList;

public class myDsl_ReactConfigurations  {

    private String name;





    private myDsl_ReactConfiguration mydsl_reactconfiguration;


    public myDsl_ReactConfigurations(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_ReactConfiguration getMydsl_reactconfiguration() {
        return mydsl_reactconfiguration;
    }

    public void setMydsl_reactconfiguration(myDsl_ReactConfiguration mydsl_reactconfiguration) {
        this.mydsl_reactconfiguration = mydsl_reactconfiguration;
    }

}