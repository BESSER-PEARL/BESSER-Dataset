





import java.util.List;
import java.util.ArrayList;

public class easyflow_Group extends GroupingCriterion {

    private String name;





    private easyflow_StringToGroupMap easyflow_stringtogroupmap;


    public easyflow_Group(
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

    public easyflow_StringToGroupMap getEasyflow_stringtogroupmap() {
        return easyflow_stringtogroupmap;
    }

    public void setEasyflow_stringtogroupmap(easyflow_StringToGroupMap easyflow_stringtogroupmap) {
        this.easyflow_stringtogroupmap = easyflow_stringtogroupmap;
    }

}