





import java.util.List;
import java.util.ArrayList;

public class classmodel_Classifier extends Entity {

    private String constraint;



    public classmodel_Classifier(
        String constraint    ) {
        super(
        );
        this.constraint = constraint;
    }


    public String getConstraint() {
        return constraint;
    }

    public void setConstraint(String constraint) {
        this.constraint = constraint;
    }


}