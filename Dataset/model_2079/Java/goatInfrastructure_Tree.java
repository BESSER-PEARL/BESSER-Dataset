





import java.util.List;
import java.util.ArrayList;

public class goatInfrastructure_Tree extends Infrastructure {

    private String registration;





    private goatInfrastructure_TreeNode goatinfrastructure_treenode;


    public goatInfrastructure_Tree(
        String registration    ) {
        super(
        );
        this.registration = registration;
    }


    public String getRegistration() {
        return registration;
    }

    public void setRegistration(String registration) {
        this.registration = registration;
    }

    public goatInfrastructure_TreeNode getGoatinfrastructure_treenode() {
        return goatinfrastructure_treenode;
    }

    public void setGoatinfrastructure_treenode(goatInfrastructure_TreeNode goatinfrastructure_treenode) {
        this.goatinfrastructure_treenode = goatinfrastructure_treenode;
    }

}