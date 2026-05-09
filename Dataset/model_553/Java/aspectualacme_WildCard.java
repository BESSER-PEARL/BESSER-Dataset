





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_WildCard extends attachableElement {

    private String expression;





    private aspectualacme_System aspectualacme_system;




    private aspectualacme_Family aspectualacme_family;


    public aspectualacme_WildCard(
        String expression    ) {
        super(
        );
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public aspectualacme_System getAspectualacme_system() {
        return aspectualacme_system;
    }

    public void setAspectualacme_system(aspectualacme_System aspectualacme_system) {
        this.aspectualacme_system = aspectualacme_system;
    }
    public aspectualacme_Family getAspectualacme_family() {
        return aspectualacme_family;
    }

    public void setAspectualacme_family(aspectualacme_Family aspectualacme_family) {
        this.aspectualacme_family = aspectualacme_family;
    }

}