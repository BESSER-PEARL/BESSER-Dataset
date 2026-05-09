





import java.util.List;
import java.util.ArrayList;

public class eol_NameExpression extends Expression {

    private String resolvedContent;
    private boolean isType;
    private String name;



    public eol_NameExpression(
        String resolvedContent,        boolean isType,        String name    ) {
        super(
        );
        this.resolvedContent = resolvedContent;
        this.isType = isType;
        this.name = name;
    }


    public String getResolvedcontent() {
        return resolvedContent;
    }

    public void setResolvedcontent(String resolvedContent) {
        this.resolvedContent = resolvedContent;
    }
    public boolean getIstype() {
        return isType;
    }

    public void setIstype(boolean isType) {
        this.isType = isType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}