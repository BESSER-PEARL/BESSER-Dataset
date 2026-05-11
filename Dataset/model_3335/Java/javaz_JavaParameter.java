





import java.util.List;
import java.util.ArrayList;

public class javaz_JavaParameter extends JavaElement {

    private String type;
    private String kind;
    private boolean final;
    private String parameterKind;





    private javaz_Method javaz_method;


    public javaz_JavaParameter(
        String type,        String kind,        boolean final,        String parameterKind    ) {
        super(
        );
        this.type = type;
        this.kind = kind;
        this.final = final;
        this.parameterKind = parameterKind;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public String getParameterkind() {
        return parameterKind;
    }

    public void setParameterkind(String parameterKind) {
        this.parameterKind = parameterKind;
    }

    public javaz_Method getJavaz_method() {
        return javaz_method;
    }

    public void setJavaz_method(javaz_Method javaz_method) {
        this.javaz_method = javaz_method;
    }

}