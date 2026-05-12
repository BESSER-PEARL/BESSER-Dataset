




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class query_DateExpression extends Expression {

    private LocalDate value;



    public query_DateExpression(
        LocalDate value    ) {
        super(
        );
        this.value = value;
    }


    public LocalDate getValue() {
        return value;
    }

    public void setValue(LocalDate value) {
        this.value = value;
    }


}