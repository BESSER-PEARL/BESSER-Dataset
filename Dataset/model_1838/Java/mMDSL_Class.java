





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Class  {

    private String name;





    private mMDSL_Metamodel mmdsl_metamodel;




    private List<mMDSL_InsertEmbedCode> mmdsl_insertembedcodes;




    private mMDSL_SymbolClass mmdsl_symbolclass;




    private mMDSL_Class mmdsl_class;


    public mMDSL_Class(
        String name    ) {
        this.name = name;
        this.mmdsl_insertembedcodes = new ArrayList<>();
    }

    public mMDSL_Class(
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

    public mMDSL_Metamodel getMmdsl_metamodel() {
        return mmdsl_metamodel;
    }

    public void setMmdsl_metamodel(mMDSL_Metamodel mmdsl_metamodel) {
        this.mmdsl_metamodel = mmdsl_metamodel;
    }
    public List<mMDSL_InsertEmbedCode> getMmdsl_insertembedcodes() {
        return mmdsl_insertembedcodes;
    }

    public void addMmdsl_insertembedcode(Mmdsl_insertembedcode mmdsl_insertembedcode) {
        this.mmdsl_insertembedcodes.add(mmdsl_insertembedcode);
    }
    public mMDSL_SymbolClass getMmdsl_symbolclass() {
        return mmdsl_symbolclass;
    }

    public void setMmdsl_symbolclass(mMDSL_SymbolClass mmdsl_symbolclass) {
        this.mmdsl_symbolclass = mmdsl_symbolclass;
    }
    public mMDSL_Class getMmdsl_class() {
        return mmdsl_class;
    }

    public void setMmdsl_class(mMDSL_Class mmdsl_class) {
        this.mmdsl_class = mmdsl_class;
    }

}