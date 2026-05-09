





import java.util.List;
import java.util.ArrayList;

public class myDsl_ReactDependenciesSubRules  {






    private List<myDsl_SingleDependencies> mydsl_singledependenciess;




    private myDsl_ReactDependenciesRules mydsl_reactdependenciesrules;


    public myDsl_ReactDependenciesSubRules(
    ) {
        this.mydsl_singledependenciess = new ArrayList<>();
    }

    public myDsl_ReactDependenciesSubRules(
        ArrayList<myDsl_SingleDependencies> mydsl_singledependenciess    ) {
        this.mydsl_singledependenciess = mydsl_singledependenciess;
    }


    public List<myDsl_SingleDependencies> getMydsl_singledependenciess() {
        return mydsl_singledependenciess;
    }

    public void addMydsl_singledependencies(Mydsl_singledependencies mydsl_singledependencies) {
        this.mydsl_singledependenciess.add(mydsl_singledependencies);
    }
    public myDsl_ReactDependenciesRules getMydsl_reactdependenciesrules() {
        return mydsl_reactdependenciesrules;
    }

    public void setMydsl_reactdependenciesrules(myDsl_ReactDependenciesRules mydsl_reactdependenciesrules) {
        this.mydsl_reactdependenciesrules = mydsl_reactdependenciesrules;
    }

}