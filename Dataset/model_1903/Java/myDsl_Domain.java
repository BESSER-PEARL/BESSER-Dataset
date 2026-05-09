





import java.util.List;
import java.util.ArrayList;

public class myDsl_Domain  {






    private List<myDsl_RelationDom> mydsl_relationdoms;




    private myDsl_System mydsl_system;


    public myDsl_Domain(
    ) {
        this.mydsl_relationdoms = new ArrayList<>();
    }

    public myDsl_Domain(
        ArrayList<myDsl_RelationDom> mydsl_relationdoms    ) {
        this.mydsl_relationdoms = mydsl_relationdoms;
    }


    public List<myDsl_RelationDom> getMydsl_relationdoms() {
        return mydsl_relationdoms;
    }

    public void addMydsl_relationdom(Mydsl_relationdom mydsl_relationdom) {
        this.mydsl_relationdoms.add(mydsl_relationdom);
    }
    public myDsl_System getMydsl_system() {
        return mydsl_system;
    }

    public void setMydsl_system(myDsl_System mydsl_system) {
        this.mydsl_system = mydsl_system;
    }

}