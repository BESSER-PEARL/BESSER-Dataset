





import java.util.List;
import java.util.ArrayList;

public class behaviour_Literal extends Expression {

    private String vlaue;



    public behaviour_Literal(
        String vlaue    ) {
        super(
        );
        this.vlaue = vlaue;
    }


    public String getVlaue() {
        return vlaue;
    }

    public void setVlaue(String vlaue) {
        this.vlaue = vlaue;
    }


}