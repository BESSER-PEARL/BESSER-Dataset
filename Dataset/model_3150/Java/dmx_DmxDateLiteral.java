




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class dmx_DmxDateLiteral extends DExpression {

    private LocalDate value;



    public dmx_DmxDateLiteral(
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