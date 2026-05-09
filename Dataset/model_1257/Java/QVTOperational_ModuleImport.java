





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ModuleImport  {

    private String kind;





    private Module module;




    private Module module;




    private List<ModelType> modeltypes;


    public QVTOperational_ModuleImport(
        String kind    ) {
        this.kind = kind;
        this.modeltypes = new ArrayList<>();
    }

    public QVTOperational_ModuleImport(
        String kind        ArrayList<ModelType> modeltypes    ) {
        this.kind = kind;
        this.modeltypes = modeltypes;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public Module getModule() {
        return module;
    }

    public void setModule(Module module) {
        this.module = module;
    }
    public Module getModule() {
        return module;
    }

    public void setModule(Module module) {
        this.module = module;
    }
    public List<ModelType> getModeltypes() {
        return modeltypes;
    }

    public void addModeltype(Modeltype modeltype) {
        this.modeltypes.add(modeltype);
    }

}