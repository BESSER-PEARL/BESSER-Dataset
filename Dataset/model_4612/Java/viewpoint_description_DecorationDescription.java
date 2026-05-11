





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DecorationDescription  {

    private String decoratorPath;
    private String name;
    private String preconditionExpression;
    private String position;



    public viewpoint_description_DecorationDescription(
        String decoratorPath,        String name,        String preconditionExpression,        String position    ) {
        this.decoratorPath = decoratorPath;
        this.name = name;
        this.preconditionExpression = preconditionExpression;
        this.position = position;
    }


    public String getDecoratorpath() {
        return decoratorPath;
    }

    public void setDecoratorpath(String decoratorPath) {
        this.decoratorPath = decoratorPath;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }


}