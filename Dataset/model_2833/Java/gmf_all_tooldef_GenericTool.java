





import java.util.List;
import java.util.ArrayList;

public class gmf_all_tooldef_GenericTool extends AbstractTool {

    private String toolClass;



    public gmf_all_tooldef_GenericTool(
        String toolClass    ) {
        super(
        );
        this.toolClass = toolClass;
    }


    public String getToolclass() {
        return toolClass;
    }

    public void setToolclass(String toolClass) {
        this.toolClass = toolClass;
    }


}