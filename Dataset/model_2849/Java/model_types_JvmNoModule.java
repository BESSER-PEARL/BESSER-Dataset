





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmNoModule  {






    private List<types_model_EObject> types_model_eobjects;




    private XImportSection1 ximportsection1;


    public model_types_JvmNoModule(
    ) {
        this.types_model_eobjects = new ArrayList<>();
    }

    public model_types_JvmNoModule(
        ArrayList<types_model_EObject> types_model_eobjects    ) {
        this.types_model_eobjects = types_model_eobjects;
    }


    public List<types_model_EObject> getTypes_model_eobjects() {
        return types_model_eobjects;
    }

    public void addTypes_model_eobject(Types_model_eobject types_model_eobject) {
        this.types_model_eobjects.add(types_model_eobject);
    }
    public XImportSection1 getXimportsection1() {
        return ximportsection1;
    }

    public void setXimportsection1(XImportSection1 ximportsection1) {
        this.ximportsection1 = ximportsection1;
    }

}