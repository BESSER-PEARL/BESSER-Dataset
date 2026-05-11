





import java.util.List;
import java.util.ArrayList;

public class myDsl_designator  {

    private String identifier;





    private myDsl_designator_list mydsl_designator_list;


    public myDsl_designator(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public myDsl_designator_list getMydsl_designator_list() {
        return mydsl_designator_list;
    }

    public void setMydsl_designator_list(myDsl_designator_list mydsl_designator_list) {
        this.mydsl_designator_list = mydsl_designator_list;
    }

}