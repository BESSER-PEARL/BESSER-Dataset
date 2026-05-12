





import java.util.List;
import java.util.ArrayList;

public class sqls_SqlStringLiteral extends SqlExpr {

    private String value;



    public sqls_SqlStringLiteral(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}