





import java.util.List;
import java.util.ArrayList;

public class model6_ReferenceObject extends BaseObject {






    private model6_BaseObject model6_baseobject;




    private List<model6_BaseObject> model6_baseobjects;


    public model6_ReferenceObject(
    ) {
        super(
        );
        this.model6_baseobjects = new ArrayList<>();
    }

    public model6_ReferenceObject(
        ArrayList<model6_BaseObject> model6_baseobjects    ) {
        this.model6_baseobjects = model6_baseobjects;
    }


    public model6_BaseObject getModel6_baseobject() {
        return model6_baseobject;
    }

    public void setModel6_baseobject(model6_BaseObject model6_baseobject) {
        this.model6_baseobject = model6_baseobject;
    }
    public List<model6_BaseObject> getModel6_baseobjects() {
        return model6_baseobjects;
    }

    public void addModel6_baseobject(Model6_baseobject model6_baseobject) {
        this.model6_baseobjects.add(model6_baseobject);
    }

}