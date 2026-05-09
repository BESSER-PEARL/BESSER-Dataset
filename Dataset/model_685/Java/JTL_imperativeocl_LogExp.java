





import java.util.List;
import java.util.ArrayList;

public class JTL_imperativeocl_LogExp extends ImperativeExpression {

    private String text;
    private int level;





    private OclExpression oclexpression;


    public JTL_imperativeocl_LogExp(
        String text,        int level    ) {
        super(
        );
        this.text = text;
        this.level = level;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}