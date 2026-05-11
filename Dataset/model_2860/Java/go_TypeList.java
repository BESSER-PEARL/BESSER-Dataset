





import java.util.List;
import java.util.ArrayList;

public class go_TypeList  {






    private List<go_Type> go_types;




    private go_TypeSwitchCase go_typeswitchcase;


    public go_TypeList(
    ) {
        this.go_types = new ArrayList<>();
    }

    public go_TypeList(
        ArrayList<go_Type> go_types    ) {
        this.go_types = go_types;
    }


    public List<go_Type> getGo_types() {
        return go_types;
    }

    public void addGo_type(Go_type go_type) {
        this.go_types.add(go_type);
    }
    public go_TypeSwitchCase getGo_typeswitchcase() {
        return go_typeswitchcase;
    }

    public void setGo_typeswitchcase(go_TypeSwitchCase go_typeswitchcase) {
        this.go_typeswitchcase = go_typeswitchcase;
    }

}