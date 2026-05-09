





import java.util.List;
import java.util.ArrayList;

public class kermeta_behavior_CallVariable extends CallExpression {

    private String isAtpre;



    public kermeta_behavior_CallVariable(
        String isAtpre    ) {
        super(
        );
        this.isAtpre = isAtpre;
    }


    public String getIsatpre() {
        return isAtpre;
    }

    public void setIsatpre(String isAtpre) {
        this.isAtpre = isAtpre;
    }


}