





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Attribute  {

    private String name;
    private String access;





    private mMDSL_Relation mmdsl_relation;




    private mMDSL_Class mmdsl_class;




    private mMDSL_Metamodel mmdsl_metamodel;


    public mMDSL_Attribute(
        String name,        String access    ) {
        this.name = name;
        this.access = access;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccess() {
        return access;
    }

    public void setAccess(String access) {
        this.access = access;
    }

    public mMDSL_Relation getMmdsl_relation() {
        return mmdsl_relation;
    }

    public void setMmdsl_relation(mMDSL_Relation mmdsl_relation) {
        this.mmdsl_relation = mmdsl_relation;
    }
    public mMDSL_Class getMmdsl_class() {
        return mmdsl_class;
    }

    public void setMmdsl_class(mMDSL_Class mmdsl_class) {
        this.mmdsl_class = mmdsl_class;
    }
    public mMDSL_Metamodel getMmdsl_metamodel() {
        return mmdsl_metamodel;
    }

    public void setMmdsl_metamodel(mMDSL_Metamodel mmdsl_metamodel) {
        this.mmdsl_metamodel = mmdsl_metamodel;
    }

}