





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DecorationDescription  {

    private String imageExpression;
    private String position;
    private String distributionDirection;
    private String preconditionExpression;
    private String tooltipExpression;
    private String name;



    public viewpoint_description_DecorationDescription(
        String imageExpression,        String position,        String distributionDirection,        String preconditionExpression,        String tooltipExpression,        String name    ) {
        this.imageExpression = imageExpression;
        this.position = position;
        this.distributionDirection = distributionDirection;
        this.preconditionExpression = preconditionExpression;
        this.tooltipExpression = tooltipExpression;
        this.name = name;
    }


    public String getImageexpression() {
        return imageExpression;
    }

    public void setImageexpression(String imageExpression) {
        this.imageExpression = imageExpression;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getDistributiondirection() {
        return distributionDirection;
    }

    public void setDistributiondirection(String distributionDirection) {
        this.distributionDirection = distributionDirection;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public String getTooltipexpression() {
        return tooltipExpression;
    }

    public void setTooltipexpression(String tooltipExpression) {
        this.tooltipExpression = tooltipExpression;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}