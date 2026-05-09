





import java.util.List;
import java.util.ArrayList;

public class eol_NameExpression extends Expression {

    private String name;
    private String resolvedContent;



    public eol_NameExpression(
        String name,        String resolvedContent    ) {
        super(
        );
        this.name = name;
        this.resolvedContent = resolvedContent;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getResolvedcontent() {
        return resolvedContent;
    }

    public void setResolvedcontent(String resolvedContent) {
        this.resolvedContent = resolvedContent;
    }


}