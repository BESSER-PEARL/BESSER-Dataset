





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Mode  {

    private String name;





    private List<mMDSL_Class> mmdsl_classs;




    private List<mMDSL_Relation> mmdsl_relations;




    private mMDSL_ModelType mmdsl_modeltype;


    public mMDSL_Mode(
        String name    ) {
        this.name = name;
        this.mmdsl_classs = new ArrayList<>();
        this.mmdsl_relations = new ArrayList<>();
    }

    public mMDSL_Mode(
        String name        ArrayList<mMDSL_Class> mmdsl_classs,        ArrayList<mMDSL_Relation> mmdsl_relations    ) {
        this.name = name;
        this.mmdsl_classs = mmdsl_classs;
        this.mmdsl_relations = mmdsl_relations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mMDSL_Class> getMmdsl_classs() {
        return mmdsl_classs;
    }

    public void addMmdsl_class(Mmdsl_class mmdsl_class) {
        this.mmdsl_classs.add(mmdsl_class);
    }
    public List<mMDSL_Relation> getMmdsl_relations() {
        return mmdsl_relations;
    }

    public void addMmdsl_relation(Mmdsl_relation mmdsl_relation) {
        this.mmdsl_relations.add(mmdsl_relation);
    }
    public mMDSL_ModelType getMmdsl_modeltype() {
        return mmdsl_modeltype;
    }

    public void setMmdsl_modeltype(mMDSL_ModelType mmdsl_modeltype) {
        this.mmdsl_modeltype = mmdsl_modeltype;
    }

}