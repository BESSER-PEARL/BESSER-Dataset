





import java.util.List;
import java.util.ArrayList;

public class sequence_description_FrameMapping extends description_DelimitedEventMapping, description_ContainerMapping {

    private String coveredLifelinesExpression;
    private String centerLabelExpression;



    public sequence_description_FrameMapping(
        String coveredLifelinesExpression,        String centerLabelExpression    ) {
        super(
        );
        this.coveredLifelinesExpression = coveredLifelinesExpression;
        this.centerLabelExpression = centerLabelExpression;
    }


    public String getCoveredlifelinesexpression() {
        return coveredLifelinesExpression;
    }

    public void setCoveredlifelinesexpression(String coveredLifelinesExpression) {
        this.coveredLifelinesExpression = coveredLifelinesExpression;
    }
    public String getCenterlabelexpression() {
        return centerLabelExpression;
    }

    public void setCenterlabelexpression(String centerLabelExpression) {
        this.centerLabelExpression = centerLabelExpression;
    }


}