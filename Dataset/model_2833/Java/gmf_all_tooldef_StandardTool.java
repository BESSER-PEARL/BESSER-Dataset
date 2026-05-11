





import java.util.List;
import java.util.ArrayList;

public class gmf_all_tooldef_StandardTool extends AbstractTool {

    private String toolKind;



    public gmf_all_tooldef_StandardTool(
        String toolKind    ) {
        super(
        );
        this.toolKind = toolKind;
    }


    public String getToolkind() {
        return toolKind;
    }

    public void setToolkind(String toolKind) {
        this.toolKind = toolKind;
    }


}