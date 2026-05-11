





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_VariableBinding  {






    private OPLmetamodel_Expression oplmetamodel_expression;




    private OPLmetamodel_RelationalInit oplmetamodel_relationalinit;




    private List<OPLmetamodel_BindingRef> oplmetamodel_bindingrefs;


    public OPLmetamodel_VariableBinding(
    ) {
        this.oplmetamodel_bindingrefs = new ArrayList<>();
    }

    public OPLmetamodel_VariableBinding(
        ArrayList<OPLmetamodel_BindingRef> oplmetamodel_bindingrefs    ) {
        this.oplmetamodel_bindingrefs = oplmetamodel_bindingrefs;
    }


    public OPLmetamodel_Expression getOplmetamodel_expression() {
        return oplmetamodel_expression;
    }

    public void setOplmetamodel_expression(OPLmetamodel_Expression oplmetamodel_expression) {
        this.oplmetamodel_expression = oplmetamodel_expression;
    }
    public OPLmetamodel_RelationalInit getOplmetamodel_relationalinit() {
        return oplmetamodel_relationalinit;
    }

    public void setOplmetamodel_relationalinit(OPLmetamodel_RelationalInit oplmetamodel_relationalinit) {
        this.oplmetamodel_relationalinit = oplmetamodel_relationalinit;
    }
    public List<OPLmetamodel_BindingRef> getOplmetamodel_bindingrefs() {
        return oplmetamodel_bindingrefs;
    }

    public void addOplmetamodel_bindingref(Oplmetamodel_bindingref oplmetamodel_bindingref) {
        this.oplmetamodel_bindingrefs.add(oplmetamodel_bindingref);
    }

}