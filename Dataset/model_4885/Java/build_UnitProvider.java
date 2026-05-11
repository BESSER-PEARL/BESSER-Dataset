





import java.util.List;
import java.util.ArrayList;

public class build_UnitProvider extends BExpression {

    private String documentation;



    public build_UnitProvider(
        String documentation    ) {
        super(
        );
        this.documentation = documentation;
    }


    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }


}