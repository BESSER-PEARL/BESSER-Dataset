





import java.util.List;
import java.util.ArrayList;

public class transformation_FeatureAccess extends Expression {

    private boolean nullable;
    private boolean spreading;



    public transformation_FeatureAccess(
        boolean nullable,        boolean spreading    ) {
        super(
        );
        this.nullable = nullable;
        this.spreading = spreading;
    }


    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public boolean getSpreading() {
        return spreading;
    }

    public void setSpreading(boolean spreading) {
        this.spreading = spreading;
    }


}