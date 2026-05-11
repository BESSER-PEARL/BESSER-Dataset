





import java.util.List;
import java.util.ArrayList;

public class simplejava_Type  {

    private String typeName;





    private simplejava_Method simplejava_method;




    private simplejava_Parameter simplejava_parameter;




    private simplejava_ClassDeclaration simplejava_classdeclaration;


    public simplejava_Type(
        String typeName    ) {
        this.typeName = typeName;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }

    public simplejava_Method getSimplejava_method() {
        return simplejava_method;
    }

    public void setSimplejava_method(simplejava_Method simplejava_method) {
        this.simplejava_method = simplejava_method;
    }
    public simplejava_Parameter getSimplejava_parameter() {
        return simplejava_parameter;
    }

    public void setSimplejava_parameter(simplejava_Parameter simplejava_parameter) {
        this.simplejava_parameter = simplejava_parameter;
    }
    public simplejava_ClassDeclaration getSimplejava_classdeclaration() {
        return simplejava_classdeclaration;
    }

    public void setSimplejava_classdeclaration(simplejava_ClassDeclaration simplejava_classdeclaration) {
        this.simplejava_classdeclaration = simplejava_classdeclaration;
    }

}