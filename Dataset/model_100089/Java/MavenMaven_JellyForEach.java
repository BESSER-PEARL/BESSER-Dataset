





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_JellyForEach extends JellyCommand {

    private String items;
    private String indexVar;
    private String var;





    private ContentsGoal contentsgoal;


    public MavenMaven_JellyForEach(
        String items,        String indexVar,        String var    ) {
        super(
        );
        this.items = items;
        this.indexVar = indexVar;
        this.var = var;
    }


    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }
    public String getIndexvar() {
        return indexVar;
    }

    public void setIndexvar(String indexVar) {
        this.indexVar = indexVar;
    }
    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }

    public ContentsGoal getContentsgoal() {
        return contentsgoal;
    }

    public void setContentsgoal(ContentsGoal contentsgoal) {
        this.contentsgoal = contentsgoal;
    }

}