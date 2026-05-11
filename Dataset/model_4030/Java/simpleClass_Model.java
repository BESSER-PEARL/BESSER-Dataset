





import java.util.List;
import java.util.ArrayList;

public class simpleClass_Model  {






    private List<simpleClass_Class> simpleclass_classs;


    public simpleClass_Model(
    ) {
        this.simpleclass_classs = new ArrayList<>();
    }

    public simpleClass_Model(
        ArrayList<simpleClass_Class> simpleclass_classs    ) {
        this.simpleclass_classs = simpleclass_classs;
    }


    public List<simpleClass_Class> getSimpleclass_classs() {
        return simpleclass_classs;
    }

    public void addSimpleclass_class(Simpleclass_class simpleclass_class) {
        this.simpleclass_classs.add(simpleclass_class);
    }

}