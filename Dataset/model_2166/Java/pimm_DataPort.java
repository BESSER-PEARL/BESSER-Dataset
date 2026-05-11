





import java.util.List;
import java.util.ArrayList;

public class pimm_DataPort extends Port {

    private String annotation;





    private pimm_Expression pimm_expression;


    public pimm_DataPort(
        String annotation    ) {
        super(
        );
        this.annotation = annotation;
    }


    public String getAnnotation() {
        return annotation;
    }

    public void setAnnotation(String annotation) {
        this.annotation = annotation;
    }

    public pimm_Expression getPimm_expression() {
        return pimm_expression;
    }

    public void setPimm_expression(pimm_Expression pimm_expression) {
        this.pimm_expression = pimm_expression;
    }

}