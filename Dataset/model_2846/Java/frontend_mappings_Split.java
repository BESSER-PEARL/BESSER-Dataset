





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_Split extends Operator {






    private List<ClassMapping> classmappings;


    public frontend_mappings_Split(
    ) {
        super(
        );
        this.classmappings = new ArrayList<>();
    }

    public frontend_mappings_Split(
        ArrayList<ClassMapping> classmappings    ) {
        this.classmappings = classmappings;
    }


    public List<ClassMapping> getClassmappings() {
        return classmappings;
    }

    public void addClassmapping(Classmapping classmapping) {
        this.classmappings.add(classmapping);
    }

}