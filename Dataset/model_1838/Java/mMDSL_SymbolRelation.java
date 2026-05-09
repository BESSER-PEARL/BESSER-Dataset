





import java.util.List;
import java.util.ArrayList;

public class mMDSL_SymbolRelation  {

    private String name;





    private mMDSL_SymbolStyle mmdsl_symbolstyle;




    private mMDSL_Method mmdsl_method;


    public mMDSL_SymbolRelation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mMDSL_SymbolStyle getMmdsl_symbolstyle() {
        return mmdsl_symbolstyle;
    }

    public void setMmdsl_symbolstyle(mMDSL_SymbolStyle mmdsl_symbolstyle) {
        this.mmdsl_symbolstyle = mmdsl_symbolstyle;
    }
    public mMDSL_Method getMmdsl_method() {
        return mmdsl_method;
    }

    public void setMmdsl_method(mMDSL_Method mmdsl_method) {
        this.mmdsl_method = mmdsl_method;
    }

}