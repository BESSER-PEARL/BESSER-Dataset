





import java.util.List;
import java.util.ArrayList;

public class UML_Activity_mine_ObjectNode extends ActivityNode {

    private String upperBound;
    private String objects;



    public UML_Activity_mine_ObjectNode(
        String upperBound,        String objects    ) {
        super(
        );
        this.upperBound = upperBound;
        this.objects = objects;
    }


    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }
    public String getObjects() {
        return objects;
    }

    public void setObjects(String objects) {
        this.objects = objects;
    }


}