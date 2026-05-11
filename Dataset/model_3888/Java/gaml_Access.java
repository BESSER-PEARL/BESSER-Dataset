





import java.util.List;
import java.util.ArrayList;

public class gaml_Access extends Expression {

    private String named_exp;



    public gaml_Access(
        String named_exp    ) {
        super(
        );
        this.named_exp = named_exp;
    }


    public String getNamed_exp() {
        return named_exp;
    }

    public void setNamed_exp(String named_exp) {
        this.named_exp = named_exp;
    }


}