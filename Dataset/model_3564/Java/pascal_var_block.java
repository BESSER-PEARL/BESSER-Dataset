





import java.util.List;
import java.util.ArrayList;

public class pascal_var_block  {






    private pascal_Pascal pascal_pascal;




    private List<pascal_EObject> pascal_eobjects;


    public pascal_var_block(
    ) {
        this.pascal_eobjects = new ArrayList<>();
    }

    public pascal_var_block(
        ArrayList<pascal_EObject> pascal_eobjects    ) {
        this.pascal_eobjects = pascal_eobjects;
    }


    public pascal_Pascal getPascal_pascal() {
        return pascal_pascal;
    }

    public void setPascal_pascal(pascal_Pascal pascal_pascal) {
        this.pascal_pascal = pascal_pascal;
    }
    public List<pascal_EObject> getPascal_eobjects() {
        return pascal_eobjects;
    }

    public void addPascal_eobject(Pascal_eobject pascal_eobject) {
        this.pascal_eobjects.add(pascal_eobject);
    }

}