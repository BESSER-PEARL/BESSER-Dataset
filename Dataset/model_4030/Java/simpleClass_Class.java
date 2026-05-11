





import java.util.List;
import java.util.ArrayList;

public class simpleClass_Class  {

    private String name;





    private List<simpleClass_Class> simpleclass_classs;


    public simpleClass_Class(
        String name    ) {
        this.name = name;
        this.simpleclass_classs = new ArrayList<>();
    }

    public simpleClass_Class(
        String name        ArrayList<simpleClass_Class> simpleclass_classs    ) {
        this.name = name;
        this.simpleclass_classs = simpleclass_classs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<simpleClass_Class> getSimpleclass_classs() {
        return simpleclass_classs;
    }

    public void addSimpleclass_class(Simpleclass_class simpleclass_class) {
        this.simpleclass_classs.add(simpleclass_class);
    }

}