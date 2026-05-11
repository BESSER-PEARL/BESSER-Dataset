





import java.util.List;
import java.util.ArrayList;

public class typedef_TDDocumentation  {

    private String doc;





    private typedef_Feature typedef_feature;




    private typedef_Type typedef_type;


    public typedef_TDDocumentation(
        String doc    ) {
        this.doc = doc;
    }


    public String getDoc() {
        return doc;
    }

    public void setDoc(String doc) {
        this.doc = doc;
    }

    public typedef_Feature getTypedef_feature() {
        return typedef_feature;
    }

    public void setTypedef_feature(typedef_Feature typedef_feature) {
        this.typedef_feature = typedef_feature;
    }
    public typedef_Type getTypedef_type() {
        return typedef_type;
    }

    public void setTypedef_type(typedef_Type typedef_type) {
        this.typedef_type = typedef_type;
    }

}