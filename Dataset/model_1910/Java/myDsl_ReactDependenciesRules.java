





import java.util.List;
import java.util.ArrayList;

public class myDsl_ReactDependenciesRules  {

    private String name;





    private myDsl_ReactDependencies mydsl_reactdependencies;


    public myDsl_ReactDependenciesRules(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_ReactDependencies getMydsl_reactdependencies() {
        return mydsl_reactdependencies;
    }

    public void setMydsl_reactdependencies(myDsl_ReactDependencies mydsl_reactdependencies) {
        this.mydsl_reactdependencies = mydsl_reactdependencies;
    }

}