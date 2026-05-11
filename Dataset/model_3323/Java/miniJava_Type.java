





import java.util.List;
import java.util.ArrayList;

public class miniJava_Type  {

    private String typeName;





    private miniJava_ClassDecl minijava_classdecl;




    private miniJava_Method minijava_method;


    public miniJava_Type(
        String typeName    ) {
        this.typeName = typeName;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }

    public miniJava_ClassDecl getMinijava_classdecl() {
        return minijava_classdecl;
    }

    public void setMinijava_classdecl(miniJava_ClassDecl minijava_classdecl) {
        this.minijava_classdecl = minijava_classdecl;
    }
    public miniJava_Method getMinijava_method() {
        return minijava_method;
    }

    public void setMinijava_method(miniJava_Method minijava_method) {
        this.minijava_method = minijava_method;
    }

}