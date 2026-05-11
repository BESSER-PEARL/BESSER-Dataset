





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_SimpleBasicLiteral extends SimpleLiteral {

    private String lit;



    public deviceModelingLanguage_SimpleBasicLiteral(
        String lit    ) {
        super(
        );
        this.lit = lit;
    }


    public String getLit() {
        return lit;
    }

    public void setLit(String lit) {
        this.lit = lit;
    }


}