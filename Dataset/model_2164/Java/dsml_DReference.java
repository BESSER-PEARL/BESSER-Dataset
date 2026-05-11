





import java.util.List;
import java.util.ArrayList;

public class dsml_DReference extends DEdge {

    private boolean nonGraphicalProperty;



    public dsml_DReference(
        boolean nonGraphicalProperty    ) {
        super(
        );
        this.nonGraphicalProperty = nonGraphicalProperty;
    }


    public boolean getNongraphicalproperty() {
        return nonGraphicalProperty;
    }

    public void setNongraphicalproperty(boolean nonGraphicalProperty) {
        this.nonGraphicalProperty = nonGraphicalProperty;
    }


}