





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DecorationDescription  {

    private String preconditionExpression;
    private String position;
    private String tooltipExpression;
    private String distributionDirection;
    private String imageExpression;
    private String name;



    public viewpoint_description_DecorationDescription(
        String preconditionExpression,        String position,        String tooltipExpression,        String distributionDirection,        String imageExpression,        String name    ) {
        this.preconditionExpression = preconditionExpression;
        this.position = position;
        this.tooltipExpression = tooltipExpression;
        this.distributionDirection = distributionDirection;
        this.imageExpression = imageExpression;
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
    public String getTooltipexpression() {
        return tooltipExpression;
    }

    public void setTooltipexpression(String tooltipExpression) {
        this.tooltipExpression = tooltipExpression;
    }
    public String getDistributiondirection() {
        return distributionDirection;
    }

    public void setDistributiondirection(String distributionDirection) {
        this.distributionDirection = distributionDirection;
    }
    public String getImageexpression() {
        return imageExpression;
    }

    public void setImageexpression(String imageExpression) {
        this.imageExpression = imageExpression;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}