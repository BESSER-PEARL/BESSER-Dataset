





import java.util.List;
import java.util.ArrayList;

public class easyflow_GroupingCriterion  {

    private String id;





    private easyflow_EasyFlowMetadata easyflow_easyflowmetadata;




    private easyflow_StringToGroupingCriterionMap easyflow_stringtogroupingcriterionmap;


    public easyflow_GroupingCriterion(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public easyflow_EasyFlowMetadata getEasyflow_easyflowmetadata() {
        return easyflow_easyflowmetadata;
    }

    public void setEasyflow_easyflowmetadata(easyflow_EasyFlowMetadata easyflow_easyflowmetadata) {
        this.easyflow_easyflowmetadata = easyflow_easyflowmetadata;
    }
    public easyflow_StringToGroupingCriterionMap getEasyflow_stringtogroupingcriterionmap() {
        return easyflow_stringtogroupingcriterionmap;
    }

    public void setEasyflow_stringtogroupingcriterionmap(easyflow_StringToGroupingCriterionMap easyflow_stringtogroupingcriterionmap) {
        this.easyflow_stringtogroupingcriterionmap = easyflow_stringtogroupingcriterionmap;
    }

}