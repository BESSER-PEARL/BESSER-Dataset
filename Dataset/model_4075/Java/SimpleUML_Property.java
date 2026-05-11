





import java.util.List;
import java.util.ArrayList;

public class SimpleUML_Property extends NamedElement {

    private boolean isContainment;
    private String primitiveType;





    private SimpleUML_Class simpleuml_class;




    private SimpleUML_Class simpleuml_class;


    public SimpleUML_Property(
        boolean isContainment,        String primitiveType    ) {
        super(
        );
        this.isContainment = isContainment;
        this.primitiveType = primitiveType;
    }


    public boolean getIscontainment() {
        return isContainment;
    }

    public void setIscontainment(boolean isContainment) {
        this.isContainment = isContainment;
    }
    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }

    public SimpleUML_Class getSimpleuml_class() {
        return simpleuml_class;
    }

    public void setSimpleuml_class(SimpleUML_Class simpleuml_class) {
        this.simpleuml_class = simpleuml_class;
    }
    public SimpleUML_Class getSimpleuml_class() {
        return simpleuml_class;
    }

    public void setSimpleuml_class(SimpleUML_Class simpleuml_class) {
        this.simpleuml_class = simpleuml_class;
    }

}