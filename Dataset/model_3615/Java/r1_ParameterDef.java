





import java.util.List;
import java.util.ArrayList;

public class r1_ParameterDef extends Element {

    private String name;
    private String parameterType;
    private String accessLevel;





    private r1_Expression r1_expression;




    private r1_TypeSpecifier r1_typespecifier;


    public r1_ParameterDef(
        String name,        String parameterType,        String accessLevel    ) {
        super(
        );
        this.name = name;
        this.parameterType = parameterType;
        this.accessLevel = accessLevel;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getParametertype() {
        return parameterType;
    }

    public void setParametertype(String parameterType) {
        this.parameterType = parameterType;
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
    public r1_TypeSpecifier getR1_typespecifier() {
        return r1_typespecifier;
    }

    public void setR1_typespecifier(r1_TypeSpecifier r1_typespecifier) {
        this.r1_typespecifier = r1_typespecifier;
    }

}