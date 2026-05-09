





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ExplicitConstructorInvocation  {

    private String keyword;





    private javaDsl_ConstructorBody javadsl_constructorbody;


    public javaDsl_ExplicitConstructorInvocation(
        String keyword    ) {
        this.keyword = keyword;
    }


    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public javaDsl_ConstructorBody getJavadsl_constructorbody() {
        return javadsl_constructorbody;
    }

    public void setJavadsl_constructorbody(javaDsl_ConstructorBody javadsl_constructorbody) {
        this.javadsl_constructorbody = javadsl_constructorbody;
    }

}