





import java.util.List;
import java.util.ArrayList;

public class myDsl_Type_specifier  {

    private String primitiveType;
    private String className;





    private myDsl_Type mydsl_type;


    public myDsl_Type_specifier(
        String primitiveType,        String className    ) {
        this.primitiveType = primitiveType;
        this.className = className;
    }


    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }

    public myDsl_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDsl_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }

}