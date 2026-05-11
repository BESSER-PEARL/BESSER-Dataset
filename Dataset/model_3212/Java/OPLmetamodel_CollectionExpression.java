





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_CollectionExpression extends Expression {

    private boolean isUnique;



    public OPLmetamodel_CollectionExpression(
        boolean isUnique    ) {
        super(
        );
        this.isUnique = isUnique;
    }


    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
    }


}