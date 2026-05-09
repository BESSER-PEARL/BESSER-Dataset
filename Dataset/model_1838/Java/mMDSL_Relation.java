





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Relation  {

    private String name;





    private List<mMDSL_InsertEmbedCode> mmdsl_insertembedcodes;




    private mMDSL_SymbolRelation mmdsl_symbolrelation;




    private mMDSL_Metamodel mmdsl_metamodel;




    private mMDSL_Relation mmdsl_relation;




    private mMDSL_Class mmdsl_class;




    private mMDSL_Class mmdsl_class;


    public mMDSL_Relation(
        String name    ) {
        this.name = name;
        this.mmdsl_insertembedcodes = new ArrayList<>();
    }

    public mMDSL_Relation(
        String name        ArrayList<mMDSL_InsertEmbedCode> mmdsl_insertembedcodes    ) {
        this.name = name;
        this.mmdsl_insertembedcodes = mmdsl_insertembedcodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mMDSL_InsertEmbedCode> getMmdsl_insertembedcodes() {
        return mmdsl_insertembedcodes;
    }

    public void addMmdsl_insertembedcode(Mmdsl_insertembedcode mmdsl_insertembedcode) {
        this.mmdsl_insertembedcodes.add(mmdsl_insertembedcode);
    }
    public mMDSL_SymbolRelation getMmdsl_symbolrelation() {
        return mmdsl_symbolrelation;
    }

    public void setMmdsl_symbolrelation(mMDSL_SymbolRelation mmdsl_symbolrelation) {
        this.mmdsl_symbolrelation = mmdsl_symbolrelation;
    }
    public mMDSL_Metamodel getMmdsl_metamodel() {
        return mmdsl_metamodel;
    }

    public void setMmdsl_metamodel(mMDSL_Metamodel mmdsl_metamodel) {
        this.mmdsl_metamodel = mmdsl_metamodel;
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
    public mMDSL_Class getMmdsl_class() {
        return mmdsl_class;
    }

    public void setMmdsl_class(mMDSL_Class mmdsl_class) {
        this.mmdsl_class = mmdsl_class;
    }

}