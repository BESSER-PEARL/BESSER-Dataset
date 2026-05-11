





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_StructuralFeature extends EntityModelElement {

    private boolean required;





    private classLayout2Frontend_Entity classlayout2frontend_entity;


    public classLayout2Frontend_StructuralFeature(
        boolean required    ) {
        super(
        );
        this.required = required;
    }


    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }

    public classLayout2Frontend_Entity getClasslayout2frontend_entity() {
        return classlayout2frontend_entity;
    }

    public void setClasslayout2frontend_entity(classLayout2Frontend_Entity classlayout2frontend_entity) {
        this.classlayout2frontend_entity = classlayout2frontend_entity;
    }

}