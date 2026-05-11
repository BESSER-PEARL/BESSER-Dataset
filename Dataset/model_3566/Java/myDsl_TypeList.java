





import java.util.List;
import java.util.ArrayList;

public class myDsl_TypeList  {






    private List<myDsl_Type> mydsl_types;




    private myDsl_TypeSwitchCase mydsl_typeswitchcase;




    private myDsl_Type mydsl_type;


    public myDsl_TypeList(
    ) {
        this.mydsl_types = new ArrayList<>();
    }

    public myDsl_TypeList(
        ArrayList<myDsl_Type> mydsl_types    ) {
        this.mydsl_types = mydsl_types;
    }


    public List<myDsl_Type> getMydsl_types() {
        return mydsl_types;
    }

    public void addMydsl_type(Mydsl_type mydsl_type) {
        this.mydsl_types.add(mydsl_type);
    }
    public myDsl_TypeSwitchCase getMydsl_typeswitchcase() {
        return mydsl_typeswitchcase;
    }

    public void setMydsl_typeswitchcase(myDsl_TypeSwitchCase mydsl_typeswitchcase) {
        this.mydsl_typeswitchcase = mydsl_typeswitchcase;
    }
    public myDsl_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDsl_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }

}