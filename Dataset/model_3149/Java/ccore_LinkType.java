





import java.util.List;
import java.util.ArrayList;

public class ccore_LinkType extends Attribute, EReference {

    private String twDestEvol;
    private int kind;
    private String selection;
    private boolean composition;
    private boolean group;
    private boolean mapping;
    private boolean annotation;
    private boolean aggregation;
    private int max;
    private int min;
    private String linkManager;
    private boolean twCoupled;
    private boolean hidden;





    private ccore_ViewLinkType ccore_viewlinktype;




    private ccore_BindingDesc ccore_bindingdesc;




    private ccore_TypeDefinition ccore_typedefinition;




    private ccore_TypeDefinition ccore_typedefinition;




    private ccore_Composer ccore_composer;


    public ccore_LinkType(
        String twDestEvol,        int kind,        String selection,        boolean composition,        boolean group,        boolean mapping,        boolean annotation,        boolean aggregation,        int max,        int min,        String linkManager,        boolean twCoupled,        boolean hidden    ) {
        super(
        );
        this.twDestEvol = twDestEvol;
        this.kind = kind;
        this.selection = selection;
        this.composition = composition;
        this.group = group;
        this.mapping = mapping;
        this.annotation = annotation;
        this.aggregation = aggregation;
        this.max = max;
        this.min = min;
        this.linkManager = linkManager;
        this.twCoupled = twCoupled;
        this.hidden = hidden;
    }


    public String getTwdestevol() {
        return twDestEvol;
    }

    public void setTwdestevol(String twDestEvol) {
        this.twDestEvol = twDestEvol;
    }
    public int getKind() {
        return kind;
    }

    public void setKind(int kind) {
        this.kind = kind;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public boolean getComposition() {
        return composition;
    }

    public void setComposition(boolean composition) {
        this.composition = composition;
    }
    public boolean getGroup() {
        return group;
    }

    public void setGroup(boolean group) {
        this.group = group;
    }
    public boolean getMapping() {
        return mapping;
    }

    public void setMapping(boolean mapping) {
        this.mapping = mapping;
    }
    public boolean getAnnotation() {
        return annotation;
    }

    public void setAnnotation(boolean annotation) {
        this.annotation = annotation;
    }
    public boolean getAggregation() {
        return aggregation;
    }

    public void setAggregation(boolean aggregation) {
        this.aggregation = aggregation;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public String getLinkmanager() {
        return linkManager;
    }

    public void setLinkmanager(String linkManager) {
        this.linkManager = linkManager;
    }
    public boolean getTwcoupled() {
        return twCoupled;
    }

    public void setTwcoupled(boolean twCoupled) {
        this.twCoupled = twCoupled;
    }
    public boolean getHidden() {
        return hidden;
    }

    public void setHidden(boolean hidden) {
        this.hidden = hidden;
    }

    public ccore_ViewLinkType getCcore_viewlinktype() {
        return ccore_viewlinktype;
    }

    public void setCcore_viewlinktype(ccore_ViewLinkType ccore_viewlinktype) {
        this.ccore_viewlinktype = ccore_viewlinktype;
    }
    public ccore_BindingDesc getCcore_bindingdesc() {
        return ccore_bindingdesc;
    }

    public void setCcore_bindingdesc(ccore_BindingDesc ccore_bindingdesc) {
        this.ccore_bindingdesc = ccore_bindingdesc;
    }
    public ccore_TypeDefinition getCcore_typedefinition() {
        return ccore_typedefinition;
    }

    public void setCcore_typedefinition(ccore_TypeDefinition ccore_typedefinition) {
        this.ccore_typedefinition = ccore_typedefinition;
    }
    public ccore_TypeDefinition getCcore_typedefinition() {
        return ccore_typedefinition;
    }

    public void setCcore_typedefinition(ccore_TypeDefinition ccore_typedefinition) {
        this.ccore_typedefinition = ccore_typedefinition;
    }
    public ccore_Composer getCcore_composer() {
        return ccore_composer;
    }

    public void setCcore_composer(ccore_Composer ccore_composer) {
        this.ccore_composer = ccore_composer;
    }

}