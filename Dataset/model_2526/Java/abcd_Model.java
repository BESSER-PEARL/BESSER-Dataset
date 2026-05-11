





import java.util.List;
import java.util.ArrayList;

public class abcd_Model extends NamedElt {

    private String style;





    private abcd_B abcd_b;




    private abcd_D abcd_d;




    private abcd_C abcd_c;


    public abcd_Model(
        String style    ) {
        super(
        );
        this.style = style;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public abcd_B getAbcd_b() {
        return abcd_b;
    }

    public void setAbcd_b(abcd_B abcd_b) {
        this.abcd_b = abcd_b;
    }
    public abcd_D getAbcd_d() {
        return abcd_d;
    }

    public void setAbcd_d(abcd_D abcd_d) {
        this.abcd_d = abcd_d;
    }
    public abcd_C getAbcd_c() {
        return abcd_c;
    }

    public void setAbcd_c(abcd_C abcd_c) {
        this.abcd_c = abcd_c;
    }

}