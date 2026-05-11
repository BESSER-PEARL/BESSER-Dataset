





import java.util.List;
import java.util.ArrayList;

public class sequence_description_FrameMapping extends description_ContainerMapping, description_DelimitedEventMapping {

    private String centerLabelExpression;
    private String coveredLifelinesExpression;



    public sequence_description_FrameMapping(
        String centerLabelExpression,        String coveredLifelinesExpression    ) {
        super(
        );
        this.centerLabelExpression = centerLabelExpression;
        this.coveredLifelinesExpression = coveredLifelinesExpression;
    }


    public String getCenterlabelexpression() {
        return centerLabelExpression;
    }

    public void setCenterlabelexpression(String centerLabelExpression) {
        this.centerLabelExpression = centerLabelExpression;
    }
    public String getCoveredlifelinesexpression() {
        return coveredLifelinesExpression;
    }

    public void setCoveredlifelinesexpression(String coveredLifelinesExpression) {
        this.coveredLifelinesExpression = coveredLifelinesExpression;
    }


}