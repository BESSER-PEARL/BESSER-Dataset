





import java.util.List;
import java.util.ArrayList;

public class form_Page  {

    private String title;





    private form_Page form_page;




    private form_Form form_form;




    private form_Page form_page;




    private form_Page form_page;




    private List<form_PageElement> form_pageelements;




    private form_Form form_form;




    private form_Page form_page;




    private form_PageElement form_pageelement;


    public form_Page(
        String title    ) {
        this.title = title;
        this.form_pageelements = new ArrayList<>();
    }

    public form_Page(
        String title        ArrayList<form_PageElement> form_pageelements    ) {
        this.title = title;
        this.form_pageelements = form_pageelements;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public form_Page getForm_page() {
        return form_page;
    }

    public void setForm_page(form_Page form_page) {
        this.form_page = form_page;
    }
    public form_Form getForm_form() {
        return form_form;
    }

    public void setForm_form(form_Form form_form) {
        this.form_form = form_form;
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
    public form_Form getForm_form() {
        return form_form;
    }

    public void setForm_form(form_Form form_form) {
        this.form_form = form_form;
    }
    public form_Page getForm_page() {
        return form_page;
    }

    public void setForm_page(form_Page form_page) {
        this.form_page = form_page;
    }
    public form_PageElement getForm_pageelement() {
        return form_pageelement;
    }

    public void setForm_pageelement(form_PageElement form_pageelement) {
        this.form_pageelement = form_pageelement;
    }

}