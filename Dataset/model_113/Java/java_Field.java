





import java.util.List;
import java.util.ArrayList;

public class java_Field extends ReferenceableElement, Variable, AnnotableAndModifiable, Initializable, Member {






    private List<java_AdditionalField> java_additionalfields;


    public java_Field(
    ) {
        super(
        );
        this.java_additionalfields = new ArrayList<>();
    }

    public java_Field(
        ArrayList<java_AdditionalField> java_additionalfields    ) {
        this.java_additionalfields = java_additionalfields;
    }


    public List<java_AdditionalField> getJava_additionalfields() {
        return java_additionalfields;
    }

    public void addJava_additionalfield(Java_additionalfield java_additionalfield) {
        this.java_additionalfields.add(java_additionalfield);
    }

}