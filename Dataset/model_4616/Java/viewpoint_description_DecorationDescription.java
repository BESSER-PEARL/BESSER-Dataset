





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DecorationDescription  {

    private String name;
    private String position;
    private String preconditionExpression;
    private String decoratorPath;



    public viewpoint_description_DecorationDescription(
        String name,        String position,        String preconditionExpression,        String decoratorPath    ) {
        this.name = name;
        this.position = position;
        this.preconditionExpression = preconditionExpression;
        this.decoratorPath = decoratorPath;
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
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public String getDecoratorpath() {
        return decoratorPath;
    }

    public void setDecoratorpath(String decoratorPath) {
        this.decoratorPath = decoratorPath;
    }


}