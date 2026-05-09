





import java.util.List;
import java.util.ArrayList;

public class javaDsl_PrimaryNoNewArray extends Primary {

    private String method;
    private String literal;
    private String keyword;
    private String reference;





    private javaDsl_ClassInstanceCreationExpression javadsl_classinstancecreationexpression;




    private javaDsl_ArrayAccess javadsl_arrayaccess;


    public javaDsl_PrimaryNoNewArray(
        String method,        String literal,        String keyword,        String reference    ) {
        super(
        );
        this.method = method;
        this.literal = literal;
        this.keyword = keyword;
        this.reference = reference;
    }


    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }

    public javaDsl_ClassInstanceCreationExpression getJavadsl_classinstancecreationexpression() {
        return javadsl_classinstancecreationexpression;
    }

    public void setJavadsl_classinstancecreationexpression(javaDsl_ClassInstanceCreationExpression javadsl_classinstancecreationexpression) {
        this.javadsl_classinstancecreationexpression = javadsl_classinstancecreationexpression;
    }
    public javaDsl_ArrayAccess getJavadsl_arrayaccess() {
        return javadsl_arrayaccess;
    }

    public void setJavadsl_arrayaccess(javaDsl_ArrayAccess javadsl_arrayaccess) {
        this.javadsl_arrayaccess = javadsl_arrayaccess;
    }

}