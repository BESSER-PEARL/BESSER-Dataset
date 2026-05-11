





import java.util.List;
import java.util.ArrayList;

public class esper2Maude_LogicalOperator  {

    private String or_;
    private String and_;





    private esper2Maude_FilterOperator esper2maude_filteroperator;




    private esper2Maude_FilterFrom esper2maude_filterfrom;


    public esper2Maude_LogicalOperator(
        String or_,        String and_    ) {
        this.or_ = or_;
        this.and_ = and_;
    }


    public String getOr_() {
        return or_;
    }

    public void setOr_(String or_) {
        this.or_ = or_;
    }
    public String getAnd_() {
        return and_;
    }

    public void setAnd_(String and_) {
        this.and_ = and_;
    }

    public esper2Maude_FilterOperator getEsper2maude_filteroperator() {
        return esper2maude_filteroperator;
    }

    public void setEsper2maude_filteroperator(esper2Maude_FilterOperator esper2maude_filteroperator) {
        this.esper2maude_filteroperator = esper2maude_filteroperator;
    }
    public esper2Maude_FilterFrom getEsper2maude_filterfrom() {
        return esper2maude_filterfrom;
    }

    public void setEsper2maude_filterfrom(esper2Maude_FilterFrom esper2maude_filterfrom) {
        this.esper2maude_filterfrom = esper2maude_filterfrom;
    }

}