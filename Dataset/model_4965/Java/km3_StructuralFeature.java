





import java.util.List;
import java.util.ArrayList;

public class km3_StructuralFeature extends TypedElement {






    private List<StructuralFeature> structuralfeatures;




    private Class class;




    private List<StructuralFeature> structuralfeatures;


    public km3_StructuralFeature(
    ) {
        super(
        );
        this.structuralfeatures = new ArrayList<>();
        this.structuralfeatures = new ArrayList<>();
    }

    public km3_StructuralFeature(
        ArrayList<StructuralFeature> structuralfeatures,        ArrayList<StructuralFeature> structuralfeatures    ) {
        this.structuralfeatures = structuralfeatures;
        this.structuralfeatures = structuralfeatures;
    }


    public List<StructuralFeature> getStructuralfeatures() {
        return structuralfeatures;
    }

    public void addStructuralfeature(Structuralfeature structuralfeature) {
        this.structuralfeatures.add(structuralfeature);
    }
    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }
    public List<StructuralFeature> getStructuralfeatures() {
        return structuralfeatures;
    }

    public void addStructuralfeature(Structuralfeature structuralfeature) {
        this.structuralfeatures.add(structuralfeature);
    }

}