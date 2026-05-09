





import java.util.List;
import java.util.ArrayList;

public class emof_Property extends TypedElement, MultiplicityElement {

    private String isDerived;
    private String default;
    private String isId;
    private String isComposite;
    private String isReadOnly;





    private Property property;




    private Module module;




    private Class class;


    public emof_Property(
        String isDerived,        String default,        String isId,        String isComposite,        String isReadOnly    ) {
        super(
        );
        this.isDerived = isDerived;
        this.default = default;
        this.isId = isId;
        this.isComposite = isComposite;
        this.isReadOnly = isReadOnly;
    }


    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getIsid() {
        return isId;
    }

    public void setIsid(String isId) {
        this.isId = isId;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }

    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }
    public Module getModule() {
        return module;
    }

    public void setModule(Module module) {
        this.module = module;
    }
    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }

}