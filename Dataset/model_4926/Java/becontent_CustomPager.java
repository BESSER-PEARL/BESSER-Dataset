





import java.util.List;
import java.util.ArrayList;

public class becontent_CustomPager  {

    private String query;
    private String order;
    private String filter;
    private String className;
    private int length;
    private String template;
    private String _id_model;





    private becontent_EntityManagerPage becontent_entitymanagerpage;




    private becontent_Form becontent_form;


    public becontent_CustomPager(
        String query,        String order,        String filter,        String className,        int length,        String template,        String _id_model    ) {
        this.query = query;
        this.order = order;
        this.filter = filter;
        this.className = className;
        this.length = length;
        this.template = template;
        this._id_model = _id_model;
    }


    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }
    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }
    public String get_id_model() {
        return _id_model;
    }

    public void set_id_model(String _id_model) {
        this._id_model = _id_model;
    }

    public becontent_EntityManagerPage getBecontent_entitymanagerpage() {
        return becontent_entitymanagerpage;
    }

    public void setBecontent_entitymanagerpage(becontent_EntityManagerPage becontent_entitymanagerpage) {
        this.becontent_entitymanagerpage = becontent_entitymanagerpage;
    }
    public becontent_Form getBecontent_form() {
        return becontent_form;
    }

    public void setBecontent_form(becontent_Form becontent_form) {
        this.becontent_form = becontent_form;
    }

}