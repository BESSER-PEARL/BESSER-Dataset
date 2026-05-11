





import java.util.List;
import java.util.ArrayList;

public class mitra_Parameter  {

    private String modifier;





    private List<mitra_Annotation> mitra_annotations;




    private mitra_TypedVarDeclaration mitra_typedvardeclaration;


    public mitra_Parameter(
        String modifier    ) {
        this.modifier = modifier;
        this.mitra_annotations = new ArrayList<>();
    }

    public mitra_Parameter(
        String modifier        ArrayList<mitra_Annotation> mitra_annotations    ) {
        this.modifier = modifier;
        this.mitra_annotations = mitra_annotations;
    }

    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }

    public List<mitra_Annotation> getMitra_annotations() {
        return mitra_annotations;
    }

    public void addMitra_annotation(Mitra_annotation mitra_annotation) {
        this.mitra_annotations.add(mitra_annotation);
    }
    public mitra_TypedVarDeclaration getMitra_typedvardeclaration() {
        return mitra_typedvardeclaration;
    }

    public void setMitra_typedvardeclaration(mitra_TypedVarDeclaration mitra_typedvardeclaration) {
        this.mitra_typedvardeclaration = mitra_typedvardeclaration;
    }

}