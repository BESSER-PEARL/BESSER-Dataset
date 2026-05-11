





import java.util.List;
import java.util.ArrayList;

public class classmodel_Attribute extends Feature {

    private boolean static;
    private String implicit;





    private classmodel_Reference classmodel_reference;


    public classmodel_Attribute(
        boolean static,        String implicit    ) {
        super(
        );
        this.static = static;
        this.implicit = implicit;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getImplicit() {
        return implicit;
    }

    public void setImplicit(String implicit) {
        this.implicit = implicit;
    }

    public classmodel_Reference getClassmodel_reference() {
        return classmodel_reference;
    }

    public void setClassmodel_reference(classmodel_Reference classmodel_reference) {
        this.classmodel_reference = classmodel_reference;
    }

}