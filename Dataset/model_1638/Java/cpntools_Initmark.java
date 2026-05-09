





import java.util.List;
import java.util.ArrayList;

public class cpntools_Initmark extends DiagramElement {

    private String expression;





    private cpntools_Place cpntools_place;


    public cpntools_Initmark(
        String expression    ) {
        super(
        );
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public cpntools_Place getCpntools_place() {
        return cpntools_place;
    }

    public void setCpntools_place(cpntools_Place cpntools_place) {
        this.cpntools_place = cpntools_place;
    }

}