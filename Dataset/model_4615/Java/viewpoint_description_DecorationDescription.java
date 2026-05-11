





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DecorationDescription  {

    private String name;
    private String position;
    private String decoratorPath;
    private String preconditionExpression;



    public viewpoint_description_DecorationDescription(
        String name,        String position,        String decoratorPath,        String preconditionExpression    ) {
        this.name = name;
        this.position = position;
        this.decoratorPath = decoratorPath;
        this.preconditionExpression = preconditionExpression;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getDecoratorpath() {
        return decoratorPath;
    }

    public void setDecoratorpath(String decoratorPath) {
        this.decoratorPath = decoratorPath;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }


}