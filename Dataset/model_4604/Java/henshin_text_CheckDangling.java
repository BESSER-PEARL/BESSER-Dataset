





import java.util.List;
import java.util.ArrayList;

public class henshin_text_CheckDangling extends RuleElement {

    private boolean checkDangling;



    public henshin_text_CheckDangling(
        boolean checkDangling    ) {
        super(
        );
        this.checkDangling = checkDangling;
    }


    public boolean getCheckdangling() {
        return checkDangling;
    }

    public void setCheckdangling(boolean checkDangling) {
        this.checkDangling = checkDangling;
    }


}