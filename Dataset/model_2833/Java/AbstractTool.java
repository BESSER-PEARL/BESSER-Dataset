





import java.util.List;
import java.util.ArrayList;

public class AbstractTool  {






    private gmf_all_mappings_ToolOwner gmf_all_mappings_toolowner;




    private gmf_all_tooldef_ToolContainer gmf_all_tooldef_toolcontainer;


    public AbstractTool(
    ) {
    }



    public gmf_all_mappings_ToolOwner getGmf_all_mappings_toolowner() {
        return gmf_all_mappings_toolowner;
    }

    public void setGmf_all_mappings_toolowner(gmf_all_mappings_ToolOwner gmf_all_mappings_toolowner) {
        this.gmf_all_mappings_toolowner = gmf_all_mappings_toolowner;
    }
    public gmf_all_tooldef_ToolContainer getGmf_all_tooldef_toolcontainer() {
        return gmf_all_tooldef_toolcontainer;
    }

    public void setGmf_all_tooldef_toolcontainer(gmf_all_tooldef_ToolContainer gmf_all_tooldef_toolcontainer) {
        this.gmf_all_tooldef_toolcontainer = gmf_all_tooldef_toolcontainer;
    }

}