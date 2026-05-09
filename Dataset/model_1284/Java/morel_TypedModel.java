





import java.util.List;
import java.util.ArrayList;

public class morel_TypedModel extends NamedElement {

    private String type;





    private morel_ObjectVariable morel_objectvariable;




    private morel_Unit morel_unit;




    private morel_EPackage morel_epackage;


    public morel_TypedModel(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public morel_ObjectVariable getMorel_objectvariable() {
        return morel_objectvariable;
    }

    public void setMorel_objectvariable(morel_ObjectVariable morel_objectvariable) {
        this.morel_objectvariable = morel_objectvariable;
    }
    public morel_Unit getMorel_unit() {
        return morel_unit;
    }

    public void setMorel_unit(morel_Unit morel_unit) {
        this.morel_unit = morel_unit;
    }
    public morel_EPackage getMorel_epackage() {
        return morel_epackage;
    }

    public void setMorel_epackage(morel_EPackage morel_epackage) {
        this.morel_epackage = morel_epackage;
    }

}