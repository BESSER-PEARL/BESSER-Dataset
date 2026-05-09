





import java.util.List;
import java.util.ArrayList;

public class atem_Break extends AbstractComponent, SectionElementType {

    private String dsl_break_type;



    public atem_Break(
        String dsl_break_type    ) {
        super(
        );
        this.dsl_break_type = dsl_break_type;
    }


    public String getDsl_break_type() {
        return dsl_break_type;
    }

    public void setDsl_break_type(String dsl_break_type) {
        this.dsl_break_type = dsl_break_type;
    }


}