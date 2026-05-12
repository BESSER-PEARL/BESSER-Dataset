




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class query_DateArrayExpression extends ArrayExpression {

    private LocalDate values;



    public query_DateArrayExpression(
        LocalDate values    ) {
        super(
        );
        this.values = values;
    }


    public LocalDate getValues() {
        return values;
    }

    public void setValues(LocalDate values) {
        this.values = values;
    }


}