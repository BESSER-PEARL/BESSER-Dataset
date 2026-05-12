





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_JellyForEach extends JellyCommand {

    private String items;
    private String var;
    private String indexVar;





    private ContentsGoal contentsgoal;


    public MavenMaven_JellyForEach(
        String items,        String var,        String indexVar    ) {
        super(
        );
        this.items = items;
        this.var = var;
        this.indexVar = indexVar;
    }


    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }
    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }
    public String getIndexvar() {
        return indexVar;
    }

    public void setIndexvar(String indexVar) {
        this.indexVar = indexVar;
    }

    public ContentsGoal getContentsgoal() {
        return contentsgoal;
    }

    public void setContentsgoal(ContentsGoal contentsgoal) {
        this.contentsgoal = contentsgoal;
    }

}