





import java.util.List;
import java.util.ArrayList;

public class form_VisibilityCondition  {






    private form_Page form_page;




    private form_Page form_page;




    private List<form_PageElement> form_pageelements;


    public form_VisibilityCondition(
    ) {
        this.form_pageelements = new ArrayList<>();
    }

    public form_VisibilityCondition(
        ArrayList<form_PageElement> form_pageelements    ) {
        this.form_pageelements = form_pageelements;
    }


    public form_Page getForm_page() {
        return form_page;
    }

    public void setForm_page(form_Page form_page) {
        this.form_page = form_page;
    }
    public form_Page getForm_page() {
        return form_page;
    }

    public void setForm_page(form_Page form_page) {
        this.form_page = form_page;
    }
    public List<form_PageElement> getForm_pageelements() {
        return form_pageelements;
    }

    public void addForm_pageelement(Form_pageelement form_pageelement) {
        this.form_pageelements.add(form_pageelement);
    }

}