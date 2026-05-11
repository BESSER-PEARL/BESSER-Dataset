





import java.util.List;
import java.util.ArrayList;

public class javaz_JavaParameter extends JavaElement {

    private String kind;
    private String type;
    private String parameterKind;
    private boolean final;



    public javaz_JavaParameter(
        String kind,        String type,        String parameterKind,        boolean final    ) {
        super(
        );
        this.kind = kind;
        this.type = type;
        this.parameterKind = parameterKind;
        this.final = final;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getParameterkind() {
        return parameterKind;
    }

    public void setParameterkind(String parameterKind) {
        this.parameterKind = parameterKind;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }


}