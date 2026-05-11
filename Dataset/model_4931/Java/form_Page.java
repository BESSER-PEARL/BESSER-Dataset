





import java.util.List;
import java.util.ArrayList;

public class form_Page  {

    private String title;





    private List<form_Page> form_pages;




    private form_Page form_page;




    private form_Form form_form;




    private form_Form form_form;




    private form_Page form_page;




    private form_Page form_page;


    public form_Page(
        String title    ) {
        this.title = title;
        this.form_pages = new ArrayList<>();
    }

    public form_Page(
        String title        ArrayList<form_Page> form_pages    ) {
        this.title = title;
        this.form_pages = form_pages;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<form_Page> getForm_pages() {
        return form_pages;
    }

    public void addForm_page(Form_page form_page) {
        this.form_pages.add(form_page);
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

}