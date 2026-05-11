





import java.util.List;
import java.util.ArrayList;

public class becontent_Content extends ViewItem {

    private int limit;
    private String joinCondition;
    private String template;
    private String orderFields;
    private String style;
    private String filter;
    private String presentationFields;
    private String _id_model;





    private becontent_Entity becontent_entity;


    public becontent_Content(
        int limit,        String joinCondition,        String template,        String orderFields,        String style,        String filter,        String presentationFields,        String _id_model    ) {
        super(
        );
        this.limit = limit;
        this.joinCondition = joinCondition;
        this.template = template;
        this.orderFields = orderFields;
        this.style = style;
        this.filter = filter;
        this.presentationFields = presentationFields;
        this._id_model = _id_model;
    }


    public int getLimit() {
        return limit;
    }

    public void setLimit(int limit) {
        this.limit = limit;
    }
    public String getJoincondition() {
        return joinCondition;
    }

    public void setJoincondition(String joinCondition) {
        this.joinCondition = joinCondition;
    }
    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }
    public String getOrderfields() {
        return orderFields;
    }

    public void setOrderfields(String orderFields) {
        this.orderFields = orderFields;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getPresentationfields() {
        return presentationFields;
    }

    public void setPresentationfields(String presentationFields) {
        this.presentationFields = presentationFields;
    }
    public String get_id_model() {
        return _id_model;
    }

    public void set_id_model(String _id_model) {
        this._id_model = _id_model;
    }

    public becontent_Entity getBecontent_entity() {
        return becontent_entity;
    }

    public void setBecontent_entity(becontent_Entity becontent_entity) {
        this.becontent_entity = becontent_entity;
    }

}