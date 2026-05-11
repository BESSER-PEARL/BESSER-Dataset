





import java.util.List;
import java.util.ArrayList;

public class myDsl_designator_listR  {






    private myDsl_designator mydsl_designator;




    private myDsl_designator_list mydsl_designator_list;




    private List<myDsl_designator_listR> mydsl_designator_listrs;


    public myDsl_designator_listR(
    ) {
        this.mydsl_designator_listrs = new ArrayList<>();
    }

    public myDsl_designator_listR(
        ArrayList<myDsl_designator_listR> mydsl_designator_listrs    ) {
        this.mydsl_designator_listrs = mydsl_designator_listrs;
    }


    public myDsl_designator getMydsl_designator() {
        return mydsl_designator;
    }

    public void setMydsl_designator(myDsl_designator mydsl_designator) {
        this.mydsl_designator = mydsl_designator;
    }
    public myDsl_designator_list getMydsl_designator_list() {
        return mydsl_designator_list;
    }

    public void setMydsl_designator_list(myDsl_designator_list mydsl_designator_list) {
        this.mydsl_designator_list = mydsl_designator_list;
    }
    public List<myDsl_designator_listR> getMydsl_designator_listrs() {
        return mydsl_designator_listrs;
    }

    public void addMydsl_designator_listr(Mydsl_designator_listr mydsl_designator_listr) {
        this.mydsl_designator_listrs.add(mydsl_designator_listr);
    }

}