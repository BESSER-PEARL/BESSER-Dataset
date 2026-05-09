





import java.util.List;
import java.util.ArrayList;

public class mMDSL_InsertContextItem  {

    private String context;
    private String name;





    private mMDSL_ContextItem mmdsl_contextitem;


    public mMDSL_InsertContextItem(
        String context,        String name    ) {
        this.context = context;
        this.name = name;
    }


    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mMDSL_ContextItem getMmdsl_contextitem() {
        return mmdsl_contextitem;
    }

    public void setMmdsl_contextitem(mMDSL_ContextItem mmdsl_contextitem) {
        this.mmdsl_contextitem = mmdsl_contextitem;
    }

}