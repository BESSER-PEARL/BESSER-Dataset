





import java.util.List;
import java.util.ArrayList;

public class easyflow_Sample extends GroupingCriterion {

    private String name;





    private easyflow_Record easyflow_record;


    public easyflow_Sample(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public easyflow_Record getEasyflow_record() {
        return easyflow_record;
    }

    public void setEasyflow_record(easyflow_Record easyflow_record) {
        this.easyflow_record = easyflow_record;
    }

}