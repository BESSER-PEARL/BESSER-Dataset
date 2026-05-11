





import java.util.List;
import java.util.ArrayList;

public class myDsl_Model  {






    private List<myDsl_Type> mydsl_types;


    public myDsl_Model(
    ) {
        this.mydsl_types = new ArrayList<>();
    }

    public myDsl_Model(
        ArrayList<myDsl_Type> mydsl_types    ) {
        this.mydsl_types = mydsl_types;
    }


    public List<myDsl_Type> getMydsl_types() {
        return mydsl_types;
    }

    public void addMydsl_type(Mydsl_type mydsl_type) {
        this.mydsl_types.add(mydsl_type);
    }

}