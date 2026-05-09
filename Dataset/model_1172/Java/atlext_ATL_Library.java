





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_Library extends Unit {






    private List<Helper> helpers;


    public atlext_ATL_Library(
    ) {
        super(
        );
        this.helpers = new ArrayList<>();
    }

    public atlext_ATL_Library(
        ArrayList<Helper> helpers    ) {
        this.helpers = helpers;
    }


    public List<Helper> getHelpers() {
        return helpers;
    }

    public void addHelper(Helper helper) {
        this.helpers.add(helper);
    }

}