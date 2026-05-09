





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ClassInstanceCreationExpression extends StatementExpression {

    private String type;





    private javaDsl_ArgumentList javadsl_argumentlist;


    public javaDsl_ClassInstanceCreationExpression(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public javaDsl_ArgumentList getJavadsl_argumentlist() {
        return javadsl_argumentlist;
    }

    public void setJavadsl_argumentlist(javaDsl_ArgumentList javadsl_argumentlist) {
        this.javadsl_argumentlist = javadsl_argumentlist;
    }

}