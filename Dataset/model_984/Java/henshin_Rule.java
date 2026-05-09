





import java.util.List;
import java.util.ArrayList;

public class henshin_Rule extends TransformationUnit {

    private boolean injectiveMatching;
    private boolean checkDangling;





    private henshin_Rule henshin_rule;


    public henshin_Rule(
        boolean injectiveMatching,        boolean checkDangling    ) {
        super(
        );
        this.injectiveMatching = injectiveMatching;
        this.checkDangling = checkDangling;
    }


    public boolean getInjectivematching() {
        return injectiveMatching;
    }

    public void setInjectivematching(boolean injectiveMatching) {
        this.injectiveMatching = injectiveMatching;
    }
    public boolean getCheckdangling() {
        return checkDangling;
    }

    public void setCheckdangling(boolean checkDangling) {
        this.checkDangling = checkDangling;
    }

    public henshin_Rule getHenshin_rule() {
        return henshin_rule;
    }

    public void setHenshin_rule(henshin_Rule henshin_rule) {
        this.henshin_rule = henshin_rule;
    }

}