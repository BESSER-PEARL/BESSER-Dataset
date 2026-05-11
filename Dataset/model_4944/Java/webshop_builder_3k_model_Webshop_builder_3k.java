





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Webshop_builder_3k  {

    private String company_name;





    private List<webshop_builder_3k_model_Component> webshop_builder_3k_model_components;




    private List<webshop_builder_3k_model_Knowledge_base> webshop_builder_3k_model_knowledge_bases;




    private List<webshop_builder_3k_model_Page> webshop_builder_3k_model_pages;




    private webshop_builder_3k_model_Page webshop_builder_3k_model_page;




    private webshop_builder_3k_model_Page webshop_builder_3k_model_page;


    public webshop_builder_3k_model_Webshop_builder_3k(
        String company_name    ) {
        this.company_name = company_name;
        this.webshop_builder_3k_model_components = new ArrayList<>();
        this.webshop_builder_3k_model_knowledge_bases = new ArrayList<>();
        this.webshop_builder_3k_model_pages = new ArrayList<>();
    }

    public webshop_builder_3k_model_Webshop_builder_3k(
        String company_name        ArrayList<webshop_builder_3k_model_Component> webshop_builder_3k_model_components,        ArrayList<webshop_builder_3k_model_Knowledge_base> webshop_builder_3k_model_knowledge_bases,        ArrayList<webshop_builder_3k_model_Page> webshop_builder_3k_model_pages    ) {
        this.company_name = company_name;
        this.webshop_builder_3k_model_components = webshop_builder_3k_model_components;
        this.webshop_builder_3k_model_knowledge_bases = webshop_builder_3k_model_knowledge_bases;
        this.webshop_builder_3k_model_pages = webshop_builder_3k_model_pages;
    }

    public String getCompany_name() {
        return company_name;
    }

    public void setCompany_name(String company_name) {
        this.company_name = company_name;
    }

    public List<webshop_builder_3k_model_Component> getWebshop_builder_3k_model_components() {
        return webshop_builder_3k_model_components;
    }

    public void addWebshop_builder_3k_model_component(Webshop_builder_3k_model_component webshop_builder_3k_model_component) {
        this.webshop_builder_3k_model_components.add(webshop_builder_3k_model_component);
    }
    public List<webshop_builder_3k_model_Knowledge_base> getWebshop_builder_3k_model_knowledge_bases() {
        return webshop_builder_3k_model_knowledge_bases;
    }

    public void addWebshop_builder_3k_model_knowledge_base(Webshop_builder_3k_model_knowledge_base webshop_builder_3k_model_knowledge_base) {
        this.webshop_builder_3k_model_knowledge_bases.add(webshop_builder_3k_model_knowledge_base);
    }
    public List<webshop_builder_3k_model_Page> getWebshop_builder_3k_model_pages() {
        return webshop_builder_3k_model_pages;
    }

    public void addWebshop_builder_3k_model_page(Webshop_builder_3k_model_page webshop_builder_3k_model_page) {
        this.webshop_builder_3k_model_pages.add(webshop_builder_3k_model_page);
    }
    public webshop_builder_3k_model_Page getWebshop_builder_3k_model_page() {
        return webshop_builder_3k_model_page;
    }

    public void setWebshop_builder_3k_model_page(webshop_builder_3k_model_Page webshop_builder_3k_model_page) {
        this.webshop_builder_3k_model_page = webshop_builder_3k_model_page;
    }
    public webshop_builder_3k_model_Page getWebshop_builder_3k_model_page() {
        return webshop_builder_3k_model_page;
    }

    public void setWebshop_builder_3k_model_page(webshop_builder_3k_model_Page webshop_builder_3k_model_page) {
        this.webshop_builder_3k_model_page = webshop_builder_3k_model_page;
    }

}