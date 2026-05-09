





import java.util.List;
import java.util.ArrayList;

public class myDsl_AppAccess  {






    private List<myDsl_AppAccessFunctions> mydsl_appaccessfunctionss;




    private myDsl_Functionalities mydsl_functionalities;


    public myDsl_AppAccess(
    ) {
        this.mydsl_appaccessfunctionss = new ArrayList<>();
    }

    public myDsl_AppAccess(
        ArrayList<myDsl_AppAccessFunctions> mydsl_appaccessfunctionss    ) {
        this.mydsl_appaccessfunctionss = mydsl_appaccessfunctionss;
    }


    public List<myDsl_AppAccessFunctions> getMydsl_appaccessfunctionss() {
        return mydsl_appaccessfunctionss;
    }

    public void addMydsl_appaccessfunctions(Mydsl_appaccessfunctions mydsl_appaccessfunctions) {
        this.mydsl_appaccessfunctionss.add(mydsl_appaccessfunctions);
    }
    public myDsl_Functionalities getMydsl_functionalities() {
        return mydsl_functionalities;
    }

    public void setMydsl_functionalities(myDsl_Functionalities mydsl_functionalities) {
        this.mydsl_functionalities = mydsl_functionalities;
    }

}