





import java.util.List;
import java.util.ArrayList;

public class javaDsl_MethodInvocation extends StatementExpression {

    private String method;
    private String keyword;





    private javaDsl_ArgumentList javadsl_argumentlist;


    public javaDsl_MethodInvocation(
        String method,        String keyword    ) {
        super(
        );
        this.method = method;
        this.keyword = keyword;
    }


    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public javaDsl_ArgumentList getJavadsl_argumentlist() {
        return javadsl_argumentlist;
    }

    public void setJavadsl_argumentlist(javaDsl_ArgumentList javadsl_argumentlist) {
        this.javadsl_argumentlist = javadsl_argumentlist;
    }

}