





import java.util.List;
import java.util.ArrayList;

public class hutn_ContainmentSlot  {






    private List<hutn_ClassObject> hutn_classobjects;


    public hutn_ContainmentSlot(
    ) {
        this.hutn_classobjects = new ArrayList<>();
    }

    public hutn_ContainmentSlot(
        ArrayList<hutn_ClassObject> hutn_classobjects    ) {
        this.hutn_classobjects = hutn_classobjects;
    }


    public List<hutn_ClassObject> getHutn_classobjects() {
        return hutn_classobjects;
    }

    public void addHutn_classobject(Hutn_classobject hutn_classobject) {
        this.hutn_classobjects.add(hutn_classobject);
    }

}