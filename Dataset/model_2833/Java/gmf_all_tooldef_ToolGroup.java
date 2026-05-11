





import java.util.List;
import java.util.ArrayList;

public class gmf_all_tooldef_ToolGroup extends ToolContainer {

    private boolean stack;
    private boolean collapsible;





    private AbstractTool abstracttool;


    public gmf_all_tooldef_ToolGroup(
        boolean stack,        boolean collapsible    ) {
        super(
        );
        this.stack = stack;
        this.collapsible = collapsible;
    }


    public boolean getStack() {
        return stack;
    }

    public void setStack(boolean stack) {
        this.stack = stack;
    }
    public boolean getCollapsible() {
        return collapsible;
    }

    public void setCollapsible(boolean collapsible) {
        this.collapsible = collapsible;
    }

    public AbstractTool getAbstracttool() {
        return abstracttool;
    }

    public void setAbstracttool(AbstractTool abstracttool) {
        this.abstracttool = abstracttool;
    }

}