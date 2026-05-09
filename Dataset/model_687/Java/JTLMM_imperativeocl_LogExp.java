





import java.util.List;
import java.util.ArrayList;

public class JTLMM_imperativeocl_LogExp extends ImperativeExpression {

    private int level;
    private String text;



    public JTLMM_imperativeocl_LogExp(
        int level,        String text    ) {
        super(
        );
        this.level = level;
        this.text = text;
    }


    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}