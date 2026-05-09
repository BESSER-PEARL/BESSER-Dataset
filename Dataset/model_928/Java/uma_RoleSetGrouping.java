





import java.util.List;
import java.util.ArrayList;

public class uma_RoleSetGrouping extends ContentCategory {






    private List<uma_RoleSet> uma_rolesets;


    public uma_RoleSetGrouping(
    ) {
        super(
        );
        this.uma_rolesets = new ArrayList<>();
    }

    public uma_RoleSetGrouping(
        ArrayList<uma_RoleSet> uma_rolesets    ) {
        this.uma_rolesets = uma_rolesets;
    }


    public List<uma_RoleSet> getUma_rolesets() {
        return uma_rolesets;
    }

    public void addUma_roleset(Uma_roleset uma_roleset) {
        this.uma_rolesets.add(uma_roleset);
    }

}