





import java.util.List;
import java.util.ArrayList;

public class SimpleUml_Property extends NamedElement {

    private String primitiveType;
    private boolean isContainment;





    private SimpleUml_Class simpleuml_class;




    private SimpleUml_Class simpleuml_class;


    public SimpleUml_Property(
        String primitiveType,        boolean isContainment    ) {
        super(
        );
        this.primitiveType = primitiveType;
        this.isContainment = isContainment;
    }


    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }
    public boolean getIscontainment() {
        return isContainment;
    }

    public void setIscontainment(boolean isContainment) {
        this.isContainment = isContainment;
    }

    public SimpleUml_Class getSimpleuml_class() {
        return simpleuml_class;
    }

    public void setSimpleuml_class(SimpleUml_Class simpleuml_class) {
        this.simpleuml_class = simpleuml_class;
    }
    public SimpleUml_Class getSimpleuml_class() {
        return simpleuml_class;
    }

    public void setSimpleuml_class(SimpleUml_Class simpleuml_class) {
        this.simpleuml_class = simpleuml_class;
    }

}