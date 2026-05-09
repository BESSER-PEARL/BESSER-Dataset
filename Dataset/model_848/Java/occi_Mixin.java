





import java.util.List;
import java.util.ArrayList;

public class occi_Mixin extends Type {






    private List<occi_Mixin> occi_mixins;


    public occi_Mixin(
    ) {
        super(
        );
        this.occi_mixins = new ArrayList<>();
    }

    public occi_Mixin(
        ArrayList<occi_Mixin> occi_mixins    ) {
        this.occi_mixins = occi_mixins;
    }


    public List<occi_Mixin> getOcci_mixins() {
        return occi_mixins;
    }

    public void addOcci_mixin(Occi_mixin occi_mixin) {
        this.occi_mixins.add(occi_mixin);
    }

}