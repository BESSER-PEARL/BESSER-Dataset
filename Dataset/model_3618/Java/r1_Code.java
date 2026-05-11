





import java.util.List;
import java.util.ArrayList;

public class r1_Code extends Expression {

    private String code;
    private String display;



    public r1_Code(
        String code,        String display    ) {
        super(
        );
        this.code = code;
        this.display = display;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getDisplay() {
        return display;
    }

    public void setDisplay(String display) {
        this.display = display;
    }


}