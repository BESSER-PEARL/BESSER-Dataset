





import java.util.List;
import java.util.ArrayList;

public class oogen_OONewClass extends OOExpression {

    private String className;





    private List<oogen_OOExpression> oogen_ooexpressions;


    public oogen_OONewClass(
        String className    ) {
        super(
        );
        this.className = className;
        this.oogen_ooexpressions = new ArrayList<>();
    }

    public oogen_OONewClass(
        String className        ArrayList<oogen_OOExpression> oogen_ooexpressions    ) {
        this.className = className;
        this.oogen_ooexpressions = oogen_ooexpressions;
    }

    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }

    public List<oogen_OOExpression> getOogen_ooexpressions() {
        return oogen_ooexpressions;
    }

    public void addOogen_ooexpression(Oogen_ooexpression oogen_ooexpression) {
        this.oogen_ooexpressions.add(oogen_ooexpression);
    }

}