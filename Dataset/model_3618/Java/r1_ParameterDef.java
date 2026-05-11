





import java.util.List;
import java.util.ArrayList;

public class r1_ParameterDef extends Element {

    private String parameterType;
    private String name;
    private String accessLevel;





    private r1_Expression r1_expression;


    public r1_ParameterDef(
        String parameterType,        String name,        String accessLevel    ) {
        super(
        );
        this.parameterType = parameterType;
        this.name = name;
        this.accessLevel = accessLevel;
    }


    public String getParametertype() {
        return parameterType;
    }

    public void setParametertype(String parameterType) {
        this.parameterType = parameterType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccesslevel() {
        return accessLevel;
    }

    public void setAccesslevel(String accessLevel) {
        this.accessLevel = accessLevel;
    }

    public r1_Expression getR1_expression() {
        return r1_expression;
    }

    public void setR1_expression(r1_Expression r1_expression) {
        this.r1_expression = r1_expression;
    }

}