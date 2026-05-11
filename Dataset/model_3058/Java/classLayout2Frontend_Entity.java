





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_Entity extends EntityModelElement {

    private boolean isAbstract;





    private classLayout2Frontend_Association classlayout2frontend_association;




    private classLayout2Frontend_ContainerView classlayout2frontend_containerview;




    private classLayout2Frontend_Entity classlayout2frontend_entity;


    public classLayout2Frontend_Entity(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public classLayout2Frontend_Association getClasslayout2frontend_association() {
        return classlayout2frontend_association;
    }

    public void setClasslayout2frontend_association(classLayout2Frontend_Association classlayout2frontend_association) {
        this.classlayout2frontend_association = classlayout2frontend_association;
    }
    public classLayout2Frontend_ContainerView getClasslayout2frontend_containerview() {
        return classlayout2frontend_containerview;
    }

    public void setClasslayout2frontend_containerview(classLayout2Frontend_ContainerView classlayout2frontend_containerview) {
        this.classlayout2frontend_containerview = classlayout2frontend_containerview;
    }
    public classLayout2Frontend_Entity getClasslayout2frontend_entity() {
        return classlayout2frontend_entity;
    }

    public void setClasslayout2frontend_entity(classLayout2Frontend_Entity classlayout2frontend_entity) {
        this.classlayout2frontend_entity = classlayout2frontend_entity;
    }

}