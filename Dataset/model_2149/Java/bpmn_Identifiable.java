





import java.util.List;
import java.util.ArrayList;

public class bpmn_Identifiable extends EModelElement {

    private String iD;



    public bpmn_Identifiable(
        String iD    ) {
        super(
        );
        this.iD = iD;
    }


    public String getId() {
        return iD;
    }

    public void setId(String iD) {
        this.iD = iD;
    }


}