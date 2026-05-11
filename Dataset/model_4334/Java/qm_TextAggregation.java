





import java.util.List;
import java.util.ArrayList;

public class qm_TextAggregation extends MeasureAggregation {

    private String specification;



    public qm_TextAggregation(
        String specification    ) {
        super(
        );
        this.specification = specification;
    }


    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }


}