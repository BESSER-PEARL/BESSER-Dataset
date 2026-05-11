





import java.util.List;
import java.util.ArrayList;

public class myDSL_EntityModel  {






    private List<myDSL_Type> mydsl_types;


    public myDSL_EntityModel(
    ) {
        this.mydsl_types = new ArrayList<>();
    }

    public myDSL_EntityModel(
        ArrayList<myDSL_Type> mydsl_types    ) {
        this.mydsl_types = mydsl_types;
    }


    public List<myDSL_Type> getMydsl_types() {
        return mydsl_types;
    }

    public void addMydsl_type(Mydsl_type mydsl_type) {
        this.mydsl_types.add(mydsl_type);
    }

}