





import java.util.List;
import java.util.ArrayList;

public class jpql_DateTimeExpression extends Value {

    private String value;



    public jpql_DateTimeExpression(
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