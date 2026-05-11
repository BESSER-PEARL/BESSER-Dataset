





import java.util.List;
import java.util.ArrayList;

public class miniJava_Member extends TypedDeclaration {

    private String access;





    private miniJava_TypeDeclaration minijava_typedeclaration;


    public miniJava_Member(
        String access    ) {
        super(
        );
        this.access = access;
    }


    public String getAccess() {
        return access;
    }

    public void setAccess(String access) {
        this.access = access;
    }

    public miniJava_TypeDeclaration getMinijava_typedeclaration() {
        return minijava_typedeclaration;
    }

    public void setMinijava_typedeclaration(miniJava_TypeDeclaration minijava_typedeclaration) {
        this.minijava_typedeclaration = minijava_typedeclaration;
    }

}