





import java.util.List;
import java.util.ArrayList;

public class javaDsl_FieldAccess extends LeftHandSide {

    private String keyword;
    private String field;





    private javaDsl_Primary javadsl_primary;


    public javaDsl_FieldAccess(
        String keyword,        String field    ) {
        super(
        );
        this.keyword = keyword;
        this.field = field;
    }


    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }
    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }

    public javaDsl_Primary getJavadsl_primary() {
        return javadsl_primary;
    }

    public void setJavadsl_primary(javaDsl_Primary javadsl_primary) {
        this.javadsl_primary = javadsl_primary;
    }

}