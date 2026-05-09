





import java.util.List;
import java.util.ArrayList;

public class occi_MixinBase  {






    private List<occi_AttributeState> occi_attributestates;




    private occi_Mixin occi_mixin;


    public occi_MixinBase(
    ) {
        this.occi_attributestates = new ArrayList<>();
    }

    public occi_MixinBase(
        ArrayList<occi_AttributeState> occi_attributestates    ) {
        this.occi_attributestates = occi_attributestates;
    }


    public List<occi_AttributeState> getOcci_attributestates() {
        return occi_attributestates;
    }

    public void addOcci_attributestate(Occi_attributestate occi_attributestate) {
        this.occi_attributestates.add(occi_attributestate);
    }
    public occi_Mixin getOcci_mixin() {
        return occi_mixin;
    }

    public void setOcci_mixin(occi_Mixin occi_mixin) {
        this.occi_mixin = occi_mixin;
    }

}