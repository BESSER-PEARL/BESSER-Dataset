





import java.util.List;
import java.util.ArrayList;

public class class_ClassModel  {






    private List<class_NamedElt> class_namedelts;


    public class_ClassModel(
    ) {
        this.class_namedelts = new ArrayList<>();
    }

    public class_ClassModel(
        ArrayList<class_NamedElt> class_namedelts    ) {
        this.class_namedelts = class_namedelts;
    }


    public List<class_NamedElt> getClass_namedelts() {
        return class_namedelts;
    }

    public void addClass_namedelt(Class_namedelt class_namedelt) {
        this.class_namedelts.add(class_namedelt);
    }

}